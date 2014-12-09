from django.http import HttpResponse
from django.shortcuts import render_to_response
from collections import Counter

import numpy as np
import random
import math
import re

import sqlite3
import json 

# ===================================================
#		HELPER FUNCTIONS
# ===================================================

# Check if a given string can be parsed into a number
def isNumerical(val):
        try:
                float(val)
                return 1
        except ValueError:
                return 0

# Establish connection to given database file and return sqlite3 cursor
def initialize_connection(db_filename):
    conn = sqlite3.connect(db_filename)
    conn.text_factory = str
    return conn.cursor()

# Determine list of tables in database, using provided sqlite3 cursor
def tables(c):
    table_list = []

    for row in c.execute("SELECT name FROM sqlite_master WHERE type='table';"):
	table_list.append(row[0])

    return table_list

# Get schema for a given table
def table_schema(c, table_name):
    rows = []

    for row in c.execute("pragma table_info(\'" + table_name + "\')"):
	rows.append(row)

    return rows

# Get list of column names for a given table
def table_columns(c, table_name):
    c.execute('SELECT * FROM ' + table_name + ' LIMIT 1')
    return [field_name[0] for field_name in c.description]

# Get list of data types in a given table
def table_types(c, table_name):
    return [rows[2] for rows in table_schema(c, table_name)]

# Get list of column names for the result of a given query
def query_columns(c, query):
    c.execute(query)
    return [field_name[0] for field_name in c.description]

# Evaluate query and return rows
def evaluate_query(c, query):
    rows = []

    for row in c.execute(query):
	rows.append(row)

    return rows

# Evaluate query and return random sample of rows
def sample_query(c, query, n):
    query += " ORDER BY RANDOM() LIMIT " + str(n)

    return evaluate_query(c, query)

def sample_column(c, table, column, n):
    query = 'SELECT ' + table + '.' + column + ' FROM ' + table + ' WHERE ' + table + '.' + column + ' NOT null'
    rows = sample_query(c, query, n)

    return [row[0] for row in rows]

def seq_column(c, table, column, n):
    query = 'SELECT ' + table + '.' + column + ' FROM ' + table + ' WHERE ' + table + '.' + column + ' NOT null LIMIT ' + str(n)
    rows = evaluate_query(c, query)

    return [row[0] for row in rows]

def sample_columns(c, table, column1, column2, n):
    query = 'SELECT ' + table + '.' + column1 + ', ' + table + '.' + column2 + ' FROM ' + table + ' WHERE ' + table + '.' + column1 + ' NOT null AND ' + table + '.' + column2 + ' NOT null'
    rows = sample_query(c, query, n)

    return [row[0] for row in rows], [row[1] for row in rows]

def row_count(c, table):
    return evaluate_query(c, 'SELECT COUNT(*) FROM ' + table)[0][0]

# Calculate self-information for a set
def self_information(X):
    p = Counter(X)
    lns = float(len(X))

    return -sum( count/lns * math.log(count/lns, 2) for count in p.values())

# Calculate self-information for a histogrammed set
def entropy(H):
    si = 0

    tot = float(np.sum(H))

    for i in range(H.shape[0]):
	if H[i] > 0.0:
	    si += (H[i] / tot) * np.log2((H[i] / tot))

    return -si

# Calculate mutual information for two set
def mutual_information(H):
    mi = 0

    tot = float(np.sum(H))

    for i in range(H.shape[0]):
        for j in range(H.shape[1]):
            fx = np.sum(H[i,:]) / tot
            fy = np.sum(H[:,j]) / tot
            if (fx > 0.0 and fy > 0.0 and H[i,j] > 0.0):
                mi += (H[i,j] / tot) * np.log2( (H[i,j] / tot) / (fx * fy))

    return mi

def generate_id():
    return ''.join(random.choice('ABCDEFGHIJKL123456789') for i in range(16))


# ===================================================
#		    VIEWS
# ===================================================

# Initialize session and return list of tables in database file
def get_tables(request):
    # Get filename from request
    filename = request.GET.get('f', '')

    # Get list of tablenames from database
    c = initialize_connection(filename)
    table_names = tables(c)

    # Set filename for this session
    request.session['filename'] = filename

    return HttpResponse(json.dumps(table_names), content_type="application/json")

# For a given table in the database, determine good queries using heuristics
# Return list of queries and chart types
def make_queries(request):
    # Get tablename from request
    table = request.GET.get('table_name', '')

    # TODO: delete the lines below this
    if table == 'tablename1':
        return HttpResponse({'pie_chart':'sql_query'});

    if table == '':
	return HttpResponse('No table name specified!')

    c = initialize_connection(request.session.get('filename', ''))
    columns = table_columns(c, table)
    types = table_types(c, table)
    nr = row_count(c, table)

    read_max = 100000

    # Generate categorical chart using self-information scheme 
    sin_max = 0; 
    i_max = -1;

    mi_max = 0;
    i2_max = -1;
    j2_max = -1;

    for i, t in enumerate(types):
	if ('char' in t):
	    # Heuristic: only consider string entries with less than 100 chars
	    print t
	    if int(re.sub('\D', '', t)) <= 100:
		# Sample at most read_max rows
		if nr < read_max: 
		    X = sample_column(c, table, columns[i], math.floor(0.5 * nr))
		else:
		    X = seq_column(c, table, columns[i], read_max)
		l = len(Counter(X))
		si = self_information(X)
		if l > 0:
		    sin = si / l
		    if sin > sin_max:
			i_max = i
			sin_max = sin

		    print columns[i], sin

	for j in range(i + 1, len(types)):
	    if (('double' in types[i]) or ('double' in types[i])) and (('double' in types[j]) or ('double' in types[j])):
		if nr < read_max:
		    X, Y = sample_columns(c, table, columns[i], columns[j], math.floor(0.3 * nr))
		else:
		    X, Y = sample_columns(c, table, columns[i], columns[j], read_max)

		TBD = 100 # Replace this with sensible binning algo
		H, xedges, yedges = np.histogram2d(X, Y, bins=TBD)
		mi = mutual_information(H)

		if mi > mi_max:
		    mi_max = mi
		    i2_max = i
		    j2_max = j

    # Introduce handling for case where q1 or q2 or q3 cannot be generated 
    q1 = ''
    q2 = ''

    if not (i_max == -1):
	q1 = 'SELECT ' + table + '.' + columns[i_max] + ' FROM ' + table + ' WHERE ' + table + '.' + columns[i_max] + ' NOT null '
    if not (i2_max == -1) and not (j2_max == -1):
	q2 = 'SELECT ' + table + '.' + columns[i2_max] + ', ' + table + '.' + columns[j2_max] + ' FROM ' + table + ' WHERE ' + table + '.' + columns[i2_max] + ' NOT null AND ' + table + '.' + columns[j2_max] + ' NOT null '

    #return HttpResponse("<p>" + q1 + "</p><p>" + q2 + "</p>")
    return HttpResponse(q1)

    # Generate distribution chart using self-information scheme
    # Generate functional chart using mutual-information scheme
    # Generate word cloud based on heuristics for string characteristics?

    # Return list of chart_type and chart_id pairs
    #return HttpResponse(test_id)

# Process an arbitrary query and return data arranged appropriately for a given chart type
def process_query(request):
    chart_type = request.GET.get('chart_type', '')
    query = request.GET.get('query', '')

    if chart_type == '':
	return HttpResponse('No chart type specified!')

    # Execute query and fetch rows
    c = initialize_connection(request.session.get('filename', ''))
    rows = evaluate_query(c, query)

    # Organize into JSON according to chart type 
    # PIE CHART -- if 1d, use Counter, if 2d, string field is dict key
    # HISTOGRAM -- 1d, use np.histogram
    # LINE CHART -- 2d, return in order as float

# ===================================================
#		    OTHER
# ===================================================

# Handle query from a PIE CHART card (or any two-dimensional requester eventually)  
def pie_chart(request):

	# Open connection to database; currently just a file
	conn = sqlite3.connect(request.GET.get('d',''));
	c = conn.cursor()
	
	# Variable to hold query output as dictionary
	response_data = {}

	# Assuming TWO-COLUMN output from query, put string-type value as key of a dictionary
	for row in c.execute(request.GET.get('q','')): 
		if isNumerical(row[0]):
			response_data[row[1]] = row[0]
		else:
			response_data[row[0]] = row[1]

	# Construct a JSON from dictionary and return
	return HttpResponse(json.dumps(response_data), content_type="application/json")
	
# Handle query from a WORD CLOUD card (or any two-dimensional requester eventually)  
def word_cloud(request):
	return render_to_response('/DBPlotter/static/bubble_cloud/index.html')

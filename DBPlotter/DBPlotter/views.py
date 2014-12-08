from django.http import HttpResponse
from django.shortcuts import render_to_response
from collections import Counter

import numpy as np
import random
import math

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


# ===================================================
#		    VIEWS
# ===================================================

# Initialize session and return list of tables in database file
def get_tables(request):
    filename = request.GET.get('f', '')

    c = initialize_connection(filename)
    table_names = enumerate_tables(c)

    return HttpResponse(json.dumps(table_names), content_type="application/json")

# For a given table in the database, determine good charts using heuristics
# Return list of chart types and chart ids
def make_charts(request):
    pass

# Provided a chart id (that the client got from make_charts), return chart data
def get_chart(request):
    pass

# Process an arbitrary query and return data arranged appropriately for a given chart type
def process_query(request):
    pass

# End session
def close(request):
    pass

# ===================================================
#		    OTHER
# ===================================================

# Handle query from a PIE CHART card (or any two-dimensional requester eventually)  
def pie_chart(request):

	# Print query for debugging purposes
	print request.GET.get('q','')
	print request.GET.get('d','')

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

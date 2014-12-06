from django.http import HttpResponse

import sqlite3
import json 

# TODO: Eventually have error checking; for example, not two-column, or neither is number
# TODO: Fix browser compatibility issues (flickering, scattered card in Safari)

# TODO: Better color scheme for pie chart (in JS) 
# TODO: Add a 1D chart (word cloud) 
# TODO: Fix page formatting (and font) and add more description and sample queries

# TODO: Polish up server configuration and clean up useless files
# TODO: Clean up JS code
# TODO: Implement proper REST API 

# IDEA: Intelligently process data of various dimensionalities into a chart type
# IDEA: Automatically generate basic charts for a database


# Helper function to check if a given string can be parsed into a number
def isNumerical(val):
	try:
		float(val)
		return 1
	except ValueError:
		return 0

# Establish connection to given database file and return sqlite3 cursor
def initialize_connection(db_filename):
    conn = sqlite3.connect(db_filename)
    return conn.cursor()

# Determine list of tables in database, using provided sqlite3 cursor
def enumerate_tables(c):
    tables = []

    for row in c.execute("SELECT name FROM sqlite_master WHERE type='table';"):
        tables.append(row[0].encode('ascii', 'ignore'))

    return tables


def get_tables(request):
    filename = request.GET.get('f', '')

    c = initialize_connection(filename)
    table_names = enumerate_tables(c)
    
    return HttpResponse(json.dumps(table_names), content_type="application/json")
	

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

	# Print query for debugging purposes
	print request.GET.get('q','')

	# Open connection to database; currently just a file
	conn = sqlite3.connect(databaseFile);
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
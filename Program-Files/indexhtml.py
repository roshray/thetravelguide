#!/usr/bin/python
import cgi                   # Using python CGI for the website 
from tgnlp import *          # This does all the required Natural Language Processing
from querygenerator import * # This generates the SPARQL query from the processed Natural Language Query.
from queryexecutor import *  # This executes the SPARL query and fetches the output.

# HTML Content
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print '<link rel="stylesheet" type="text/css" href="/index.css">'
print("<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css'>")
print("<title>Travel Guide</title></head>")
print("<body></br>")
print("<pre>")
print '<div align="center">'
print("<h1>TRAVEL GUIDE</h1>")
print("<h2>Plan your trip with us</h2>")
print '<form method="post" action="default.py">'
print '<input type="text" name="tbox" placeholder="Search..." required" class="txtbox">'
print '<input type="submit" value="Search" class="button" />'
print "</form>"
print "</div>"

# Getting the User query from the website
form=cgi.FieldStorage()
if form.getvalue("tbox"):
	 nlquery=form.getvalue("tbox") # Fetching the User query - Natural Language Query

processedNLQuery=processNLQuery(nlquery) # The user query is then send for Natural Language Processing and returns processed Natural Language Query

sparqlQueries=generateSparqlQuery(processedNLQuery);# The Processed Query is converted into a set of Sparql Queries.

for sparqlQuery in sparqlQueries: 
	sparqlQuery[0]=sparqlQuery[0].replace("_"," ")
	sparqlQuery[1]=sparqlQuery[1].replace("_"," ")
	print "\n"+sparqlQuery[0], # Printing the output headers 
	print " "+sparqlQuery[1]   # Like Mehrangarh Fort - Description.
	if sparqlQuery[1] is "coordinates":
		print("Unicode error")  # UTF - 8 error - TODO.
		continue
	if "?object" in sparqlQuery[2]:
		ans=quexec(sparqlQuery[2],u'object')	# Executing the queries		
		for i in ans: # Printing the output
			print i
		continue
	if "?predicate" in sparqlQuery[2]:
		ans=quexec(sparqlQuery[2],u'predicate') # Executing the queries
		for i in ans: # Printing the output
			print i
		continue
	if "?subject" in sparqlQuery:
		ans=quexec(sparqlQuery[2],u'subject') # Executing the queries
		for i in ans: # Printing the output
			print i
		continue
print("</pre>")	
print("</body></html>") #HTML ENDS

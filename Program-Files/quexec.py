from SPARQLWrapper import SPARQLWrapper, JSON              # Importing SPARQL Wrapper to run SPARQL Query and fetches output 

def quexec(query,x):						                           # Method take Query input and Type of Query
	sparql = SPARQLWrapper("http://localhost:3030/ds/query") # URI for Apache Jena Fuseki Server 
	sparql.setQuery(query)					                         # Setting the query
	sparql.setReturnFormat(JSON)				                     # Setting return type as JSON
	rawresults = sparql.query().convert()			               # Executing query, fetching and storing data 
	lis=rawresults[u'results'][u'bindings']			             # Extracting required data from the raw result
	l=list()						                                     # Creating list
	for i in lis:						                                 
		dic=dict(i)					                                   # Adding to Dictionary 
		l.append(dic[x][u'value'])			                       # Cleaning raw data.
	return l;						                                     # Returning clean extracted data.  

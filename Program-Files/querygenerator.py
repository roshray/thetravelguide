import operator
def newlineremover(x):
	y=""
	for i in range(len(x)-1):
		y+=x[i]
	return y
	

def listgenerator():
	c=0
	f=open("place.txt",'r')
	places=[[]]
	for i in range(100):
		x=f.readline()
		y=newlineremover(x)
		if(x == "\n"):
			c+=1
			places.append([])
			continue
		places[c].append(y)
	places.pop()
	return places
#def querykeywords():
#	return l
def dictsort(d):
	lis=sorted(d.items(), key=operator.itemgetter(1), reverse=True)
	return lis;
def makepair(l1,l2):
	lis1=[i[0] for i in l1 if i[1]!=0]
	lis2=[i[0] for i in l2 if i[1]!=0]
	lis=[]
	l=list()
	for i in lis1:
		for j in lis2:
			l=[]				
			l.append(i)
			l.append(j)
			lis.append(l)
	return lis;
	
def quegen(l):
	g=open("subject.txt",'r')
	interrogatives=["what","where","when","how","who"]
	city=["gaya","ajmer","amer","jaipur","bharatpur","patna","chittorgarh","udaipur","deeg","jaisalmer","mount","abu","bodh","gaya","udaipur","pali","jodhpur","bikaner","rajasamand","mandore","nalanda","pushkar","madhopur","kanoi","sasaram","tanot","bundi","thanesar","gurgaon","rohtek","chhat","bilaspur","kurukshetra","panchkula","para","pinjore","jhajjar","ranakpur"]
	state=["rajasthan","bihar","uttarpradesh","haryana"]
	attributes=["district","time","city","coordinate","description","food","history","language","photos","pincode","review","state"]	
	places=listgenerator()
	dictsub={}
	dictpre={}
	dictcity={}
	for i in range(0,100):
		r=g.readline()
		r=newlineremover(r)
		dictsub[r]=0
	dictpre={"District":0,"best_time_to_visit":0,"coordinates":0,"description":1,"reviews":0,"languages_spoken":0,"description":0,"city":0,"pincode":0,"famous_food":0,"history":0,"state":0,"photos":0,"Alias":0}
	for i in city:
		dictcity[i]=0
	dictsubkeys=dictsub.keys()
	dictprekeys=dictpre.keys()
	dictcitykeys=dictcity.keys()
	for i in l:
		if i in "what":
			dictpre["description"]+=1
			dictpre["photos"]+=1
			continue
		if i in "where":
			dictpre["District"]+=1
			dictpre["coordinates"]+=1
			dictpre["city"]+=1
			dictpre["pincode"]+=1
			dictpre["city"]+=1
			dictpre["state"]+=1
			continue
		if i in "when":
			dictpre["best_time_to_visit"]+=1
			continue
		if i in "how":
			dictpre["District"]+=1
			dictpre["coordinates"]+=1
			dictpre["city"]+=1
			dictpre["pincode"]+=1
			dictpre["city"]+=1
			dictpre["state"]+=1
			continue
		if i in "who":
			dictpre["history"]+=1
			continue
		for j in dictsubkeys:
			if i in j.lower():
				dictsub[j]+=1
		for j in dictprekeys:
			if i in j.lower():
				dictpre[j]+=1
		for j in dictcitykeys:
			if i in j.lower():
				dictcity[j]+=1
						
	#print dictsub	
	#print dictpre	
	#print dictcity
	dictpre["description"]=+0.5  #ultimate level of jugaad.
	sortedsub=dictsort(dictsub)
	sortedpre=dictsort(dictpre)
	sortedcity=dictsort(dictcity)
	subpre=makepair(sortedsub,sortedpre)
	subcity=makepair(sortedsub,sortedcity)
	precity=makepair(sortedpre,sortedcity)
	#print subpre
	#print subcity
	#print precity
	quelist=list()
	que=list()
	#[WARNING] ranking of each dictionary is left. 
	if len(subpre) is not 0:
		for i in subpre:
			s="""PREFIX ak: <http://www.semanticweb.org/ontologies/2015/8/Ontology1443603331487.owl#>
PREFIX aj: <http://www.semanticweb.org/ontologies/2015/8/Ontologytajmahalnew.owl#>
SELECT ?object
WHERE {
ak:"""+i[0]+" ak:"+i[1]+""" ?object 
}"""
			que=[]
			que.append(i[0])
			que.append(i[1])
			que.append(s)
			quelist.append(que)
	if len(subcity) is not 0:
		for i in subcity:
			s="""PREFIX ak: <http://www.semanticweb.org/ontologies/2015/8/Ontology1443603331487.owl#>
PREFIX aj: <http://www.semanticweb.org/ontologies/2015/8/Ontologytajmahalnew.owl#>
SELECT ?predicate
WHERE {
 ak:"""+i[0]+" ?predicate "+"ak:"+i[1]+""" 
}"""
			que=[]
			que.append(i[0])
			que.append(i[1])
			que.append(s)
			quelist.append(que)
	if len(precity) is not 0:
		for i in precity:
			s="""PREFIX ak: <http://www.semanticweb.org/ontologies/2015/8/Ontology1443603331487.owl#>
PREFIX aj: <http://www.semanticweb.org/ontologies/2015/8/Ontologytajmahalnew.owl#>
SELECT ?subject
WHERE {
?subject ak:"""+i[0]+" ak:"+i[1]+""" 
}"""
			que=[]
			que.append(i[0])
			que.append(i[1])
			que.append(s)
			quelist.append(que)
	return quelist;
	#print sortedsub
	#print sortedpre
	#print sortedcity	
	#print "\nSubject:"
	#for j in sortedsub:
	#	if j[1]!=0:
	#		print j[0]
	#print "\nPredictate:"		
	#for j in sortedpre:
	#	if j[1]!=0:
	#		print j[0]
	#print "\nsome of the objects:"
	#for j in sortedcity:
	#	if j[1]!=0:
	#		print j[0]

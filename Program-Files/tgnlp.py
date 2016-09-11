from nltk.stem import WordNetLemmatizer #
from nltk.tokenize import word_tokenize # To divide the NLQuery to chunks of words
from nltk.corpus import stopwords       # This is for removing stopwords like(is,the,a,an,...) which means nothing relevant.
from nltk.stem import PorterStemmer     # 
from spellcheck import *                # Corrects the spelling of the words as per the bigtext file.
from replacepattern import *            # Replaces short forms like 't, 'd to not, would/could etc.
from repeatchar import *                # Corrects the Repeated Characters in a word like "Yeaaaaah!" becomes "yeah"

def processNLQuery(nlq):
	f=open("big.txt",'a')                 #
	lemmatizer=WordNetLemmatizer()        #
	stemmer=PorterStemmer()               #
	nlq=replace(nlq)                      #
	words=word_tokenize(nlq)              #
	lwr=[word.lower() for word in words]  # 	
	rpchar=[repchar(word) for word in lwr] #repeated characters
	splchk=[correct(word) for word in rpchar] #spelling check
	stopw=set(stopwords.words('english')) #extracting stop words	
	filteredstopwords=[word for word in splchk if word not in stopw] #removing stop words
	#stemmed=[stemmer.stem(word) for word in filteredstopwords] #
	lemmatized=[lemmatizer.lemmatize(word) for word in filteredstopwords] #	
	for word in lemmatized:               #
		f.write(word + " ")                 #
	f.close()                             #
	return lemmatized;                    #

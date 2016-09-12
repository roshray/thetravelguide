from nltk.stem import WordNetLemmatizer #
from nltk.tokenize import word_tokenize # To divide the NLQuery to chunks of words
from nltk.corpus import stopwords       # This is for removing stopwords like(is,the,a,an,...) which means nothing relevant.
from nltk.stem import PorterStemmer     # 
from spellcheck import *                # Corrects the spelling of the words as per the bigtext file.
from replacepattern import *            # Replaces short forms like 't, 'd to not, would/could etc.
from repeatchar import *                # Corrects the Repeated Characters in a word like "Yeaaaaah!" becomes "yeah"

def processNLQuery(nlq):
	lemmatizer=WordNetLemmatizer()        # initializing lemmatizer from WordNet
	stemmer=PorterStemmer()               # initializing stemmer from PorterStemmer
	nlq=replace(nlq)                      # Replacing all short-form words like 't,'d,'m to not,would,am etc.
	words=word_tokenize(nlq)              # Separating words from the NLQuery and storing it in a list
	lwr=[word.lower() for word in words]  # Converting all letters to lower case to uniformity	
	rpchar=[repchar(word) for word in lwr] # Corrects repeated characters in a word (yeaaaaaaah! to yeah!)
	splchk=[correct(word) for word in rpchar] # Checking spellings of the words and correcting them if necessary using a wordbase(big.txt)
	stopw=set(stopwords.words('english')) # extracting stop words(Words those are not relevant in this context ex: is,the,a,an..
	filteredstopwords=[word for word in splchk if word not in stopw] # removing stop words from the NLQuery
	#stemmed=[stemmer.stem(word) for word in filteredstopwords] # Stemming the words
	lemmatized=[lemmatizer.lemmatize(word) for word in filteredstopwords] #	Converting the words to root form (feet-> foot, cars->car)
	f=open("big.txt",'a')                 # Opening file which is our wordbase, this is used in spellcheck. Words are appended so that spellcheck algorithm can be improved which works on probability on # of occurrence of words.
	for word in lemmatized:                
		f.write(word + " ")           #	writing words in the wordbase
	f.close()                             # closing file (wordbase)
	return lemmatized;                    # returning the Processed Query.

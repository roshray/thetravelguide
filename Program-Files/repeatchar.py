import re
from nltk.corpus import wordnet
repeat_regexp = re.compile(r'(\w*)(\w)\2(\w*)')
repl = r'\1\2\3'
def repchar(word):
	if wordnet.synsets(word):
		return word
	repl_word = repeat_regexp.sub(repl, word)
	if repl_word != word:
		return repchar(repl_word)
	else:
		return repl_word

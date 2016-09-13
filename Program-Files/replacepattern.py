import re
replacement_patterns = [ 
(r'won\'t', 'will not'),
(r'can\'t', 'can not'),
(r'i\'m', 'i am'),
(r'ain\'t', 'is not'),
(r'(\w+)\'ll', '\g<1> will'),
(r'(\w+)n\'t', '\g<1> not'),
(r'(\w+)\'ve', '\g<1> have'),
(r'(\w+)\'s', '\g<1> is'),
(r'(\w+)\'re', '\g<1> are'),
(r'(\w+)\'d', '\g<1> would'),
(r'wanna', 'want to'),
(r'gonna', 'going to'),
(r'lyk', 'like'),
(r'4', 'for'),
(r' u ', 'you')
] 
replacement_patterns = [(re.compile(regex),repl) for (regex, repl) in replacement_patterns]
def replace(text):
	s = text
	for (pattern, repl) in replacement_patterns:
		(s, count) = re.subn(pattern, repl, s)
	return s

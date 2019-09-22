word=open( "http://thinkpython2.com/code/words.txt")
def has_no_e(word):
	for letter in word:
		if letter == 'e':
		return False
	return True
has_no_e(word)
	

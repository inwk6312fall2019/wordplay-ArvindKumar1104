word=open("http://thinkpython3.com/code/word.txt")
def three_cons(s):
	i=0
	count=0
	while i<len(s)-1:
		if s[i]==s[i+1]:
			count+=1
			i+=2
			if count ==3:
				print("found")
			else:
				count=0
				i+=1
		return ("not found",count)
s=input("enter the any string")
print(three_consecutive(s))


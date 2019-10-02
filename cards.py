import random
class Deckcards:
	a=list()
	b=list()
	def __init__(self):
		for key in range(4):
			for card in range(13):
				mycards=cards(key,card)
				Deckcards.a.append(mycards)
	def __str__(self):
		for key in Deckcards.a:
			Deckcards.b.append(str(key))
		return "\n".join(Deckcards.b)
	def shuff(self):
		self.ca=[]
		self.remaining=[]
		for key in range(5):
			self.ca.append(random.choice(Deckcards.b))
		for key in self.ca:
			print(key)
		return self.c
class Numberofcards:
	def __init__(self,one,two):
		suit=["spade","heart","diamond","clubs"]
		rank=["ace",2,3,4,5,6,7,8,9,10,"jack","queen","king"]
		self.suit1=suit[one]
		self.rank1=rank[two]
	def __str__(self):
		return (self.rank1,self.suit1)
d=Deckofcards()
print("number of cards in deck")
print(d)
numberofplayers=int(input("enter the number of players")
dic=dict()
for key in range(numberofplayers):
	dic[key]=str(d.shuff())
print(dic)

num=range( 1, int(input())+1)
mydict={}
for n in num:
	mydict.update({n : n*n})
	
print(mydict)



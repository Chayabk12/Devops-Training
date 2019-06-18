print("Enter name")

name = input()
print("Enter age")
age = int(input())
if name == 'Alice':
	print('Hi',name)
elif age < 12: 
	print('you are not alice, kiddo')
elif age>100 and age <2000:
	print('your nt alice, grannie')
else: 
	print('unlike you, alice undead, imortal vampire')


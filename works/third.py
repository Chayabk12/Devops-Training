name=''
condition=True
while(condition):
	print('who are you')
	name=input()
	if(name!='joe'):
		continue
	else:
		print("Hello Joe, What is password?(it is fish)");
		password=input();
		if(password =='swoardfish'):
			#condition=False;
			break;

print('Access Granted')


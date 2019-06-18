print('please enter number')
number=int(input())
num=number
s=0
while(num>0):
	a= num%10
	s=s+a
	num=int(num/10)
	
if number%s==0:
	print('harshad number')
else:
	print('not harshad number')
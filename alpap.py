n=input()
l=0
m=0
for i in n:
	if i.isalpha():
		l=l+1
	elif i.isnumeric():
		m=m+1
if l+m==len(n) and l>0 and m>0:
	print('yes')
else :
	print('no')

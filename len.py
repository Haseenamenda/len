n=input()
c=0
k=0
for i in n:
	if(i.isalpha()):
		c=c+1
	elif(i.isnumeric()):
		k=k+1
if c+k==len(n) and c>0 and k>0:
	print("yes")
else:
	print("no")
	

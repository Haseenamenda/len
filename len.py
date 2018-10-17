n=input()
j=0
g=0
for i in n:
	if(i.isalpha()):
		j=j+1
	elif(i.isnumeric()):
		g=g+1
if j+g==len(n) and j>0 and g>0:
	print("yes")
else:
	print("no")
	

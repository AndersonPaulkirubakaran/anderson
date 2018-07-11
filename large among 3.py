x=raw_input()
y=raw_input()
z=raw_input()
a=int(x)
b=int(y)
c=int(z)
if((a>=b) and (a>=c)):
	print a
elif(b>=a) and (b>=c):
	print b
elif(c>=a) and (c>=b):	
	print c
else:
	print("invalid")

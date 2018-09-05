'''def add(a,b):
	c = a+b
	return c
print add(10,20)'''

def add(**d):
	print sum(d.values)
#add(key1=val1, key2=val2)
add(a=10, b=20, c=30)

'''def add(a,b,c=0,d=20,*e,**f):
	print a+b+c+d
add(10,20,30,40,50,60,f1=10,f2=20)'''

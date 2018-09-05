 '''#range:- this method is used to create (this method will return)
#a list of sequential no either in positive or negative direction.
# this method takes atleast one parameter atmost three parameters
#syntax: range(p1,p2,p3)
#p1 represents starting element in req seq.
#p2 represents ending element of req seq (if p2 is n then python will return a sequential list upto n-1 values)
#p3 represents either positive direction or negative direction along with no of alternative elements.
#note: default value for p1 is 1
#p2 is mandatory we should pass the value.
#p3 is default and default is 1. the output format is always a list.
s=range(0,10,2)
print s
s=range(1,10,2)
print s 
s=range(10,2,-1)
print s'''

#xrange:- 
for i in xrange(2,10,2):
	print i

'''#break:- break is keyword which is used to stop the iteration process.
	break keyword can only used in for loop.
	when ever break statement available then python will come out of loop and skip remaining iterations

l=[1,3,4,5,7]
for i in l:
	if i%2==0:
		print "list is invalid"
		break'''

'''#continue:- is a keyword which is used to skip the current iteration and start new iteration.
	this keyword should place inside the for loop.

l=[1,3,5,6,8]
for i in l:
	if i%2!=0:
		continue
		print "odd numbers", i
	else:
		print "even numbers", i'''
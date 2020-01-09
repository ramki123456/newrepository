'''l = [1, 2, 3, 4]
l.append([33, 4])
# op: [1,2,3,4,[33,4]] bcoz element can be any type that maybe datastructure
# or single element.

l.extend(15)
# op: will return error bcoz element should be datastructure

l.count(20)
# op: return o bcoz it was not in list

range(-1, -10, -1)
# op: retrun [-1,-2,-3,-4,-5,-6,-7,-8,-9]


class A:
    x = 10
obj1 = A()
obj2 = A()
print obj1.x
print id(obj1) == id(obj2)  # op: False'''

'''def percentage(stu_marks):
	for key,values in stu_marks.items():
		percentage=sum(stu_marks[key].values())/((len(stu_marks[key])*100)/100)
		print key, percentage
	
		for i in xrange(len(stu_marks[key])):
			if stu_marks[key].values()[i]>=75:
				stu_marks[key][stu_marks[key].keys()[i]]="Distinction"
			elif stu_marks[key].values()[i]>=60:
				stu_marks[key][stu_marks[key].keys()[i]]="First class"
			elif stu_marks[key].values()[i]>=50:
				stu_marks[key][stu_marks[key].keys()[i]]="Second class"
			elif stu_marks[key].values()[i]<35:
				stu_marks[key][stu_marks[key].keys()[i]]="Failed"
	return stu_marks

stu_marks={'Hari':{'Telugu':50,'English':61,'Hindi':75},
'Raju':{'Telugu':40,'English':20,'Hindi':59},
'Mahi':{'Telugu':49,'English':70,'Hindi':80},
'Nani':{'Telugu':80,'English':90,'Hindi':75}}

print percentage(stu_marks)'''

'''nums = [6,3,2,1,4,8]
new_list = []
while nums:
	minimum = nums[0]
	for x in nums:
		if x<minimum:
			minimum = x
		new_list.append(minimum)
print new_list


n='the values must go that side'
def fibb(n):
	a,b=0,1
	while b<len(n):
		print(b,end='')
		a,b=b,a+b
print(a, b)'''

'''x = {'a':1, 'b': 2}
y = {'b':10, 'c': 11}
z = dict(x.items() + y.items())
print z'''


l = [1, 2, 3, 4]
l.append([33, 4])
print l
# op: [1,2,3,4,[33,4]] bcoz element can be any type that maybe datastructure
# or single element.

l.extend('15')
print l

A = {'a':10, 'b':843, 'c': 39,'d':5,'e':300}


print(sorted(A.items(), key = 
             lambda kv:(kv[1], kv[0]), reverse=True))[:3]  
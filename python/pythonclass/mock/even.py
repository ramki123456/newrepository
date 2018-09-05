#by using break and continue:
'''for i in range(1,10):
	if i%2 == 0:
		continue
	print i'''
#by using range method.
'''for even in range(1,10):
	if even%2 == 0:
		print even'''
#by using for loop
'''l = [1,2,3,4,5,6,7,8,9,10]
for even in l:
	if even%2 == 0:
		print even'''

# by using functions.
def even(list1):
	l1 = []
	for ele in list1:
		if ele%2 == 0:
			l1.append(ele)
	return l1
print even(range(100))
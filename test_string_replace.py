'''# write a program string replace without using predefined function replace.
s, replaced_str, search_str, l = 'python', 'T', 't', []

for ele in s:
	if ele == search_str:
		ele = replaced_str
		l.append(ele)
	else:
		l.append(ele)
print ''.join(l)
       ################# or ####################
print ''.join([replaced_str if ele==search_str else ele for ele in s])


# write a program to create custom generator which takes string as input and outputs each letter
input_string = 'python'

def each_letter(strss):[(yield ele) for ele in strss]
op = each_letter(input_string)
print op.next()
print op.next()
print op.next()
print op.next()
print op.next()
print op.next()'''


# write a program which takes string as input and output each letter those many times as it has positioned in the given string 
'''s = 'string'

for loop1 in range(len(s)):
	for loop2 in range(loop1+1):
		print s[loop1],
	print "\n"
'''

s='python'
l=[]
for i in s:
	if i=='o':
		i='@'
		l.append(i)
	else:
		l.append(i)
print ''.join(l)

'''matrix = [[2 for i in xrange(3)] for i in range(5)]
print matrix'''

'''matrix=[[2 for i in xrange(3)] for i in range(5)]
print matrix'''

'''nums = [6,3,2,1,4,8]
new_list = []
while nums:
	minimum = nums[0]
	for x in nums:
		if x<minimum:
			minimum = x
		new_list.append(minimum)
print new_list

a,b=0,1
for i in range(10):
	if b<len(range(10)):
		#print (b)
		a,b=b,a+b
		print (a,b)

#sort without using inbuilt
nums = [6,3,2,1,4,8]
for i in range(len(nums)):
    for j in range(len(nums) - 1):
        if nums[j] > nums[j+1]:
            nums[j+1], nums[j] = nums[j], nums[j+1]
    print nums'''

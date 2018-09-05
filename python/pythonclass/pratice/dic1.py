l = raw_input("enter your value: ")
nums = {'0':'zero',
	'1':'one',
        '2':'two',
        '3':'three',
        '4':'four',
        '5':'five',
        '6':'six',
        '7':'seven',
        '8':'eight',
        '9':'nine',
        ":":":"}
'''for i in l:
        print nums[i],'''

s1 = ' '.join(nums[i] for i in l)
s2 = " pm"
s3 = " am"
if l>'12:00':
	x = ''.join((s1,s2))
	print x
else:
	y = ''.join((s1,s3))
	print y

'''op_data = '%s %s %s %s %s' % (nums[l[0]], nums[l[1]], nums[l[2]], nums[l[3]], nums[l[4]])
print op_data'''

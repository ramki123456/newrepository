# Loop over list of elements(Range of 100)
number = input("Enter the range for prime number sequence")

if number in (0, 1):
	print "No prime numbers"
if number > 1:
	print 2
	for ele in range(3, number+1):
		status = True
		# Check whether given element divisible in between 2 and same number
		for num in range(2, ele):
			if ele%num == 0:
				status = False
				break
			else:
				continue
		if status: print ele

'''
# Loop over list of elements(Range of 100)
number = input("Enter the range for prime number sequence")

if number in (0, 1):
	print "No prime numbers"
if number > 1:
	print 2
	for ele in range(3, number+1):
		data = [True if ele%num!=0 else False for num in range(2, ele)]
		if False in data: pass
		else:print ele
'''
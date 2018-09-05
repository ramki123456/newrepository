l=[3,4,5,7,9,11,13,1,19]
for i in l:
	for ele in range(2,i):
		if (i%ele) == 0:
			break
	else:
		print i
	#print i
for i in range(1,10):
	for ele in range(2,i):
		if(i%ele) ==  0:
			break
	else:
		print i

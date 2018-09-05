for num in range(2,8):
	# num = 7
	# [3, 4, 5, 6, 7]
	#num=7
	for i in range(2,num):
		# [2, 3, 4, 5, 6]
		# i=2
		if (num % i) == 0:
			print(num,"is not a prime number")
			break
	else:
		print(num,"is a prime number")

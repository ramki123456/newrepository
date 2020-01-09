
###################################   Task 1   ##########################################
def prime_numbers(upper, lower=2):
	return [num for num in range(2, upper) if all(num%i!=0 for i in range(2,num))]

def check_belzabar(number=None):
	if number >= 2:
		numbers = prime_numbers(1000)
		status = False
		for prime in numbers:
			if prime * (prime+14) == number or prime * (prime-14) == number:
				status = True
				break
			else:
				pass
		if status: return "Given number is Belzabar :)"
		else: return "Given number is not Belzabar :("

# print check_belzabar(51)

###################################   Task 2   ##########################################

def get_belzabar_to_million():
	belzabar_list = []
	for number in range(10000):
		if number >= 2:
			numbers = prime_numbers(100)
			status = False
			for prime in numbers:
				if prime * (prime+14) == number or prime * (prime-14) == number:
					status = True
				else:
					pass
			if status: belzabar_list.append(number)
			else: pass
		else:
			pass
	return belzabar_list, len(belzabar_list)
data = get_belzabar_to_million()
print "belzabar_numbers: {0}, Count of Belzabar Numbers : {1}".format(data[0], data[1])

###################################   Task 3   ##########################################

def get_belzabar_to_million_prime():
	return [num for num in data[0] if all(num%i!=0 for i in range(2,num))]
print get_belzabar_to_million_prime()

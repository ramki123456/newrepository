#by using range.

'''for i in range(3,100):
	for ele in range(2,i):
		if(i%ele) ==  0:
			break
	else:
		print i

#by using input method.

number = input("enter some value: ")
for i in range(3,number):
	for ele in range(2,i):
		if (i%ele) == 0:
			break
	else:
		print i'''

#by using functions.

prime_numbers = 0
'''def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True  
    for n in range(2, x):
        if x % n == 0:
            return False
    return 'given no is prime', x
print is_prime(input('enter your value: '))'''

for x in range(int(raw_input("How many numbers you wish to check: "))):
    if is_prime(x):
        prime_numbers += 1
        print x,

print "We found " + str(prime_numbers) + " prime numbers."
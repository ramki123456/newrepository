#finding a file which ends .txt and find a word
path = raw_input("enter ur path:")
library = os.listdir(path)
for book in library:
    if book.endswith('.txt'):
        file = os.path.join(book, path)
        text = open(file, 'r')

    for line in text:
        re_pattern = r'\b(:?ram)\b'
        print re.findall(re_pattern, line)

# reversing string or values

nums = "ramakrishna"
def reverse(i):
    length = len(i)
    s = length

    new_list = [None]*length

    for item in nums:
        s = s - 1
        new_list[s] = item
    return new_list
data = reverse(nums)

print "".join(data)


# class method and staticmethod

class Date(object):

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year
    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1
    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999


date1 = Date(12, 10, 1990)
date2 = Date.from_string('11-09-2012')
is_date = Date.is_date_valid('11-09-2012')

print date1.day
print date2.day
print is_date


# palindrome

def is_palindrome(string):
    for i,char in enumerate(string):
        if char != string[-i-1]:
            return False
    return True

# polymorphism

class parent(object):
    def __init__(self, name):
        self.name = name
    def talk(self):
        raise Exception('not implemented')
class cat(parent):
    def talk(self):
        return "meow"
class dog(parent):
    def talk(self):
        return "bow"

Animals = [cat(sony), dog(pinky), cat(soy)]

for Animal in Animals:
    print Animal.name+Animal.talk

# method overriding

class parent(object):
    def __init__(self):
        self.value = 5
    def get(self):
        return self.value
class child(parent):
    def get(self):
        return self.value+1

obj = child()
obj.get   ------> 6
obj = parent()
obj.get   ------> 5

# Decorator

def login(request):
    user = request.GET.get('username')
    pass = request.GET.get('password')
    us = authenticate(user, pass)
    if us.authenticated:
        login(us)
    else:
        print "invalid"

@login
def sent_box(request):
    return httpResponse("url")


# Python program to display all the prime numbers within an interval

# change the values of lower and upper for a different result
lower = 900
upper = 1000

# uncomment the following lines to take input from the user
#lower = int(input("Enter lower range: "))
#upper = int(input("Enter upper range: "))

print("Prime numbers between",lower,"and",upper,"are:")

for num in range(lower,upper + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)


# Python program to check if the input number is prime or not

num = 407

# take input from the user
# num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")

# Python Program to find the factors of a number

# define a function
def print_factors(x):
   # This function takes a number and prints the factors

   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

# change this value for a different result.
num = 320

# uncomment the following line to take input from the user
#num = int(input("Enter a number: "))

print_factors(num)


# Python program to find the factorial of a number provided by the user.

# change the value for a different result
num = 7

# uncomment to take input from the user
#num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


# Python program to find the sum of natural numbers up to n where n is provided by user

# change this value for a different result
num = 16

# uncomment to take input from the user
#num = int(input("Enter a number: "))

if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   # use while loop to iterate un till zero
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is",sum)


# Python Program to find the L.C.M. of two input number

# define a function
def lcm(x, y):
   """This function takes two
   integers and returns the L.C.M."""

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

# change the values of num1 and num2 for a different result
num1 = 54
num2 = 24

# uncomment the following lines to take input from the user
#num1 = int(input("Enter first number: "))
#num2 = int(input("Enter second number: "))

print("The L.C.M. of", num1,"and", num2,"is", lcm(num1, num2))
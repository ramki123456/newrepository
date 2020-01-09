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


# Program to check if a string
#  is palindrome or not

# change this value for a different output
my_str = 'aIbohPhoBiA'

# make it suitable for caseless comparison
my_str = my_str.casefold()

# reverse the string
rev_str = reversed(my_str)

# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
   print("It is palindrome")
else:
   print("It is not palindrome")


# Program to count the number of each vowel in a string

# string of vowels
vowels = 'aeiou'

# change this value for a different result
ip_str = 'Hello, have you tried our turorial section yet?'

# uncomment to take input from the user
#ip_str = input("Enter a string: ")

# make it suitable for caseless comparisions
ip_str = ip_str.casefold()

# make a dictionary with each vowel a key and value 0
count = {}.fromkeys(vowels,0)

# count the vowels
for char in ip_str:
   if char in count:
       count[char] += 1

print(count)


def is_palindrome(string):
    for i,char in enumerate(string):
        if char != string[-i-1]:
            return False
    return True

>>> is_palindrome('hello')
False    
>>> is_palindrome('helloolleh')
True
>>> is_palindrome('')
True
>>> is_palindrome(' ')
True
>>> is_palindrome('a')
True

def is_palindrome(string):
    result = True
    str_len = len(string)
    for i in range(0, int(str_len/2)): # you need to check only half of the string
        if string[i] != string[str_len-i-1]:
            result = False
            break
    return result # single return statement is considered a good practice


l = [1,2,[3,4], [5,6,[7,8]]]
l2 = []

for i in l:
    if type(i) is list:
        for s in range(len(i)):
            l2.append(i[s])
    else:
        l2.append(i)
print l2
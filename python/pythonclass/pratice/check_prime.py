ele = input("Enter any number:")

data = [True if ele%num!=0 else False for num in range(2, ele)]
if False not in data: print ele, "Is prime number"
else: print ele, "is not a prime number"
l = [('hari', 'banglore', 10000), ('ram', 'chennai', 12000), ('prakash', 'banglore', 18000)]
add=0
for num in l:
	if 'banglore' in num:
		add=add+num[2]
print add
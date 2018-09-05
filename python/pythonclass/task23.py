data = '''1179 hari
1180 ravi
1181 raju 
1182 kiran '''
storage = []
for numbers in data.split('\n'):
	print numbers.split()[0]


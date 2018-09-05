data='''1179 Hari
		1180 Ravi
		1181 raju
		1182 kiran'''
r=data.splitlines()
for row in r:
	idn = row.split()
	print idn
	'''def add(a,b):
		return int(a)+int(b)
	if reduce(add,idn)%3==0:
		print idn, row.split()[-1]
	else:
		pass'''
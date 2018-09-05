l=[12,3,4,5,6,7]
for i in l:
	pass
print i
l=['hari','giri']
for name in l:
	if name.endswith('i'):
		print name


l=['hari','giri']
for name in l:
	if 'i' in name:
		pass
	print name
marks=[98,68,49,96,49,82,77]
sum=0
for i in marks:
	sum=sum+i
	if i<75:
		print i, "less than 70"
print sum,'the some of given list'
print sum/len(marks),'the average of given list'


emp=[['hari','ban','ibm'],
['raju','ban','wipro'],
['ramu','chennai','ibm']]
for i in emp:
	if 'ban'in i and 'ibm' in i:
		print i


for i in [12, 16, 17, 24, 29]:
    if i % 2 == 1:  # if the number is odd
        break      # immediately exit the loop
    print(i)
print("done")
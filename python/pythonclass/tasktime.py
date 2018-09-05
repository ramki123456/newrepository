data = raw_input("enter time in HH:MM  :" )
time_data = {'0': 'Zero','1':'One',}
op=""
for ele in data:
    if ele in time_data:
         op = op + time_data(ele)
    else:
         op = op + ele
if int(data[:2])>12:
   op = op+'pm'
else:
   op = op + 'Am'
print op

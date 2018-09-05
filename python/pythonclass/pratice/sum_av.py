score = [('pak', 96), ('aus', 98), ('aus', 69), ('pak', 28), ('sa', 69), ('sa', 298)]
total_sum = 0
nation = 'pak'
for country, runs in score:
	if (country == 'pak'):
		total_sum = total_sum + runs
		average = total_sum/2
print total_sum, nation

total_sum = 0
nation = 'aus'
for country, runs in score:
	if (country == 'aus'):
		total_sum = total_sum + runs
		average = total_sum/2 
print total_sum, nation

total_sum = 0
nation = 'sa'
for country, runs in score:
	if (country == 'sa'):
		total_sum = total_sum + runs
		average = total_sum/2
print total_sum, nation
	

total_sum = total_sum + runs 
print total_sum
average = total_sum/6
print average
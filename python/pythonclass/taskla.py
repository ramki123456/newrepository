emp_sal = [5000,25000,35000,7000,9000,10000]
print reduce(lambda a,b: a+b, filter(lambda sal: sal>6000,emp_sal))

"""import sqlite3 as lite
import sys

data = (
    ('batch_no', 'item_no','cmpy_name','prc/unt','manf_dt','exp_dt','qty','delar','comment' ),
    ( 01, 521,'dettol',25,'09_2016','09_2020','500ml','sri krishna','for handwash'),
    ( 01, 522,'pears',25,'09_2016','09_2020','500gms','sri krishna','for bath'),
    ( 01, 523,'horlicks',25,'09_2016','09_2020','500gms','sri krishna','for drinking')
)

con = lite.connect('/home/brahma/Documents/EmpManagement/sqlite3.db')
with con:
    
    cur = con.cursor()    
    
    cur.execute("DROP TABLE IF EXISTS aug19")
    cur.execute("CREATE TABLE aug19('batch_no','item_no','cmpy_name','prc/unt','manf_dt','exp_dt','qty','delar','comment')")
    cur.executemany("INSERT INTO aug19 VALUES( ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)"""


'''#for retriving data
import sqlite3 as lite
import sys


con = lite.connect('pavan.db')

with con:    
    
    cur = con.cursor()    
    cur.execute("SELECT * FROM data")

    rows = cur.fetchall()

    for row in rows:
print row'''


def rightRotate(lists, num): 
    output_list = [] 
      
    # Will add values from n to the new list 
    for item in range(len(lists) - num, len(lists)): 
        output_list.append(lists[item]) 
      
    # Will add the values before 
    # n to the end of new list     
    for item in range(0, len(lists) - num):  
        #print lists[item]
        output_list.append(lists[item]) 
          
    return output_list 
  
# Driver Code 
rotate_num = 3
list_1 = [1, 2, 3, 4, 5, 6] 
 
#print(rightRotate(list_1, rotate_num))
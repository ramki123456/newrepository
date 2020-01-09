'''import collections
def largest_substring(string):
    l = list(string)
    d = collections.deque(string[1:])
    print d
    match = []
    longest_match = []
    while d:
        for i, item in enumerate(d):
            if l[i]==item:
                match.append(item)
            else:
                if len(longest_match) < len(match):
                    longest_match = match
                match = []
        d.popleft()
    return ''.join(longest_match)

print largest_substring("abccdebccfs")
'''

from itertools import combinations

def quadraples(a):
    squares = [i**2 for i in a]
    squares.sort()
    l = []
    for x,y,z in combinations(squares, 3):
        if (x+y) == z:
            print x, y, z
            if (x,y,z) not in l:
                l.extend([x,y,z])
    q = []
    for i in l:
        if i not in q:
            q.append(i)
    return q
print quadraples([3,4,5,5,5])


# Python3 Code For A Boolean Matrix Question 
R = 3
C = 4

def modifyMatrix(mat): 
    row = [0] * R 
    col = [0] * C 
    
    # Initialize all values of row[] as 0 
    for i in range(0, R): 
        row[i] = 0
        
    # Initialize all values of col[] as 0 
    for i in range(0, C) : 
        col[i] = 0


    # Store the rows and columns to be marked 
    # as 1 in row[] and col[] arrays respectively 
    for i in range(0, R) : 
        
        for j in range(0, C) : 
            if (mat[i][j] == 1) : 
                row[i] = 1
                col[j] = 1
            
    # Modify the input matrix mat[] using the 
    # above constructed row[] and col[] arrays 
    for i in range(0, R) : 
        
        for j in range(0, C): 
            if ( row[i] == 1 or col[j] == 1 ) : 
                mat[i][j] = 1
                
# A utility function to print a 2D matrix 
def printMatrix(mat) : 
    for i in range(0, R): 
        
        for j in range(0, C) : 
            print(mat[i][j], end = " ") 
        print() 
        
# Driver Code 
mat = [ [1, 0, 0, 1], 
        [0, 0, 1, 0], 
        [0, 0, 0, 0] ] 


# --> Instruction <--
# There is an array with some numbers. All numbers are equal except for one. Try to find it!

# findUniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# findUniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains at least 3 numbers.

# The tests contain some very huge arrays, so think about performance.
# --> Instruction End <--

# Solution 1 (My solution)

def find_uniq(arr):
    a,b = set(arr)
    if arr.count(a) == 1 : n = a
    else : n = b
    return n   # n: unique integer in the array
   
# Solution 2 (Best practices) 
def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b

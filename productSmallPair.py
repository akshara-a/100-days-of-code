# Perform the following function. 
# def Productsmallpair(sum,arr)

# This function accepts the integers sum and arr. It is used to find the arr(j) and arr(k), 
# where k ! = j. arr(j) and arr(k) should be the smallest elements in the array.

# Keep this in mind:
# If n<2 or empty, return –1.
# If these pairs are not found, then return to zero.
# Make sure all the values are within the integer range.
 
# Example
# Input:
# Sum: 9
# Arr: 5 4 2 3 9 1 7

# Output:
# 2

# Explanation
# From the array of integers, we have to select the two smallest numbers, i.e 2 and 1. 
# Sum of these two (2 + 1) = 3. This is less than 9 (3 < 9). The product of these two is 2 (2 x 1 = 2) Hence the output is integer 2.

# Sample input:
# Sum: 4
# Arr: 9 8 –7 3 9 3

# Sample output:
# –21

def productSmallPair(arr, sumval):
    arr.sort() 
    
    if len(arr) < 2:
        return -1 
        
    if (arr[0] + arr[1]) < sumval:
        return (arr[0] * arr[1])
    else:
        return 0 
    
    
sumval = int(input())
arr = list(map(int, input().split()))
print(productSmallPair(arr, sumval))

#############################################################################################
# Author: Dostonbek Toirov
#
#############################################################################################
# Problem: Merge an array of size n into another array of size m+n
# Taken from: geeksforgeeks.org - Google STEP Interview Experience
# Big O: O(n)
#############################################################################################

N = [5, 9, 15, 20]  #  n=4
M = [1, 3, 6, 8, 19, 35]  #  m=6

output = M[:]
output.extend(N)
n = len(N)

for i in range(len(N)):
    if output[i] < output[n]:
        continue
    else:
        output[i] = output[n]
        output[n] = N[i]
        n +=1
        print(n)

print(output)

 # Output array   N[]={1, 3, 5, 6, 8, 9, 15, 19, 20, 35}

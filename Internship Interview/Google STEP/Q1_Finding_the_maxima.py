#############################################################################################
# Author: Dostonbek Toirov
#
#############################################################################################
# Problem: Given an array of integers, find the local maxima.
# Taken from: geeksforgeeks.com - Google STEP Interview Experience
#############################################################################################


arr = [1,3,5,4,7,10,6,4,3,9,8,8,11] # input list
maxima = []                         # list to store output

for i in range(len(arr)):
    if i == 0:                      # condition for the first item in the list
        if arr[i] > arr[i+1]:       # checks only the right side, because there is nothing on the left
            maxima.append(arr[i])   # add to the list if found maxima
    elif i == len(arr) - 1:         # condition for the last item in the list
        if arr[i] > arr[i-1]:       # checks only the left side, because there is nothing on the right
            maxima.append(arr[i])   # add to the list if found maxima
    else:                           # condition for middle items
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]: # checks both sides of the item
            maxima.append(arr[i])   # add to the list if found maxima
    
print(maxima)   # prints the output on the console

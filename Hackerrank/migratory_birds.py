# Author : Dostonbek Toirov
# Time Complexity : O(n)
# Test Cases Passed : 5/6

def migratoryBirds(arr):
    mostNum = 0
    dict = {}
    
    for i in arr:
        if i not in dict.keys():
            dict[i] = 1
        else:
            dict[i] = dict[i] + 1

    for i in dict:
        if j > 2:
            m = dict[i]
            if m > n:
                mostNum = i
        n = dict[i]
    
    return mostNum

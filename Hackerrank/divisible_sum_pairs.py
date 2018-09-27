# Author : Dostonbek Toirov
# Time Complexity : O(n^2)  Not the most optimal solution

def divisibleSumPairs(n, k, ar):
    count = 0
    outputList = []
    
    for i in range(n):
        for j in range(n):
            if i < j and (ar[i] + ar[j]) % k == 0:
                outputList.append((ar[i], ar[j]))
                count += 1
    
    return count
    
# All in one line solution
# Author : LeHarkunwar

def divisibleSumPairs(n, k, ar):
    return sum(1 for i in range(n) for j in range(n) if i < j and (ar[i]+ar[j])%k == 0)

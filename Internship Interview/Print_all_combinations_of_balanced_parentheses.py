#############################################################################################
# Author: Dostonbek Toirov
#
#############################################################################################
# Problem: Print all combinations of balanced parentheses
# Taken from: geeksforgeeks.org 
# Big O: Not very sure (Using recursion)
#############################################################################################


def _printBrac(str, pos, n, open, close):
    if close == n:
        str = ''.join(str)
        print(str)
    else:
        if open > close:
            str[pos] = ')'
            _printBrac(str, pos+1, n, open, close+1)
        if open < n:
            str[pos] = '('
            _printBrac(str, pos+1, n, open+1, close)
 
def printBrac( str, n):
    if(n > 0):
        _printBrac(str, 0, n, 0, 0)

def main():    
    n = 3
    bracket_num = n * 2
    str = [None for _ in range(bracket_num)]
    printBrac(str, n);

main()


    
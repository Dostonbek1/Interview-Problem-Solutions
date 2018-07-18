####################################################################
# Author: Dostonbek Toirov
# Taken from: Leetcode
#
####################################################################

def reverse(self, x):
        s = int(str(abs(x))[::-1])
        if s > 2147483647 or s < -2147483648 :
            return 0
        return s if x > 0 else -s
        

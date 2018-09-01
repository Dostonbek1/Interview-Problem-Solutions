###########################################################
# Author : Dostonbek Toirov
# Problem from : Leetcode
#
###########################################################

def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        reverse = int(str(abs(x))[::-1])
        if reverse == x:
            return True
        else:
            return False

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <0:
            return False
        dup =x 
        reverse =0
        while (dup != 0):
            ld = dup%10
            dup = dup //10
            reverse = (reverse*10)+ld
        if (reverse == x):
            return True
        else :
            return False
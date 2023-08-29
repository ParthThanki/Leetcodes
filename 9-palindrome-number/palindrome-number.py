class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x)[0::] == str(x)[::-1]:
            return True
        else:
            return False
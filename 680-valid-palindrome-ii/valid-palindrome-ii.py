class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(p1, p2):
            while p1 < p2:
                if s[p1] == s[p2]:
                    p1 += 1
                    p2 -= 1
                else:
                    return False
            return True
        
        p1 = 0
        p2 = len(s) - 1
        
        while p1 < p2:
            if s[p1] == s[p2]:
                p1 += 1
                p2 -= 1
            else:
                return isPalindrome(p1+ 1, p2) or isPalindrome(p1, p2 -1)
        return True
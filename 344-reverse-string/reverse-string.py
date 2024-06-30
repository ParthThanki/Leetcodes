class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for n in range(len(s), 0, -1):
            s.append(s[n-1])
            s.pop(n-1)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            result = haystack.index(needle)
        except ValueError:
            result = -1

        return result
        
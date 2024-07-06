class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Start with the first string as the prefix
        prefix = strs[0]

        for i in strs[1:]:
            # Check until the prefix is not found at the start of the string `i`
            while i[:len(prefix)] != prefix:
                # Reduce the prefix by one character
                prefix = prefix[:-1]
                # If prefix becomes empty, return ""
                if not prefix:
                    return ""

        return prefix
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        combine = word1+word2

        together = ""

        for x in range(len(combine)):
            if len(word1) > x:
                together += word1[x]
                if len(word2) > x:
                    together += word2[x]
            elif len(word2) > x:
                together += word2[x]
        return together
        
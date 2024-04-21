class Solution:
    def reverseWords(self, s: str) -> str:
        """newS = s.split(" ")

        new = ""

        for num in range(len(newS),0,-1):
            if newS[num-1] == "":
                newS.remove("")
            else:
                new += newS[num-1]
                new += " "
        return(new.strip())"""
        return " ".join(reversed(s.split()))
                
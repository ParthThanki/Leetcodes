class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = ""

        for n in digits:
            temp += str(n)

        ans = int(temp) + 1

        x = [int(x) for x in str(ans)]

        return x
        
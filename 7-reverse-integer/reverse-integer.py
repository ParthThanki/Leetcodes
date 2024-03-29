class Solution:
    def reverse(self, x: int) -> int:
        numStr = str(x)
        result = ""
        hasnegative = False

        for num in reversed(range(len(numStr))):
            if numStr[num] == "-":
                hasnegative = True
            else:
                result += numStr[num]

        result = int(result)
        if hasnegative:
            result = result * -1
        if result < -2147483648 or result > 2147483647:
            return 0
        return result
                
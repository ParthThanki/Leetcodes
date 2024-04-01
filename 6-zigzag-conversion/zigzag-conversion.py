class Solution:
    def convert(self, s: str, numRows: int) -> str:
        newS = [""]*numRows
        current_row = 0
        step = -1

        if len(s) <= 1 or numRows <= 1:
            return s


        for letter in s:
            newS[current_row] += letter #inseat the char
            
            if current_row == 0 or current_row == numRows - 1:
                step = -step #change the direction to 1 so middle
            
            current_row += step #change the row to 0, 1 or 2 based on the step.

        return "".join(newS)
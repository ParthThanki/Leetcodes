class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = 0  # This will store the maximum rob sum excluding the current house
        curr = 0  # This will store the maximum rob sum including the current house
        
        for num in nums:
            # Calculate new maximum excluding current house
            temp = max(prev, curr)
            # Update current to include this house
            curr = prev + num
            # Update prev to the calculated temp
            prev = temp
        
        return max(prev, curr)
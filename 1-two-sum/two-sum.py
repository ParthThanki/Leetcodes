class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        current = 0
        loop = 1

        while True:
            if loop >= len(nums):
                loop = 0
                current += 1
            elif nums[current] + nums[loop] == target and current != loop:
                return current,loop
                break
            else:
                loop += 1
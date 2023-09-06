class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''i = 0
        j = 1

        while i <= len(nums):
            if j >= len(nums):
                return len(nums)
                break
            elif nums[i] == nums[j] and i != j:
                nums.pop(j)
                i = 0
                j = 1
            else:
                i += 1
                j += 1'''
        
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j
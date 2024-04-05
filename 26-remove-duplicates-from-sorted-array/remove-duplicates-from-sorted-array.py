class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return len(nums)
        
        count = 0

        while count < len(nums):
            if nums[count] != nums[count-1]:
                count += 1
            elif len(nums) != 1:
                nums.remove(nums[count])
            else:
                count = len(nums)
                break
        return count
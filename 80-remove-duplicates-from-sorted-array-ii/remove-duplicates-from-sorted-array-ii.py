class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return len(nums)
        
        count = 0

        while count < len(nums):
            if nums[count] != nums[count-2]:
                count += 1
            elif nums[count] == nums[count-1] and len(nums) != 2:
                nums.remove(nums[count])
            else:
                if nums[count] == nums[count+1] and len(nums) > 3:
                    nums.remove(nums[count])
                else:
                    count = len(nums)
                    break
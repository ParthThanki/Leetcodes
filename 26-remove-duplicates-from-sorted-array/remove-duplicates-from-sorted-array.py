class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        check = 0
        x = 1

        while x < len(nums):
            if nums[check] == nums[x]:
                nums.pop(check)
                x = check + 1
            else:
                check += 1
                x = check + 1


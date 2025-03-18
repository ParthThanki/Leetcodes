class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0

        while count < len(nums):
            if val == nums[count]:
                nums.pop(count)
            else:
                count+=1
        return count
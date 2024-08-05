class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        nums = nums1 + nums2
        nums.sort()

        ans = 0

        left, right = 0, len(nums) - 1

        mid = (left + right) // 2

        if len(nums) % 2 == 1:
            ans = nums[mid]
        elif len(nums) % 2 == 0:
            ans = (nums[mid] + nums[mid+1])/2
        
        return ans
        
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for num in range(n):
            nums1[m+num] = nums2[num]
        nums1.sort()
        



        
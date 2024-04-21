class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        change = 0
        while change < k:
            if len(nums) == k:
                print(nums)
                break
            elif change < k:
                nums.insert(0,nums[-1])
                del nums[-1]
                change += 1
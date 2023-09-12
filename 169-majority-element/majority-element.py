class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        checkin = []
        for i in nums:
            if i not in checkin:
                checkin.insert(i,i)
                if nums.count(i) > len(nums)/2:
                    return i
                    break
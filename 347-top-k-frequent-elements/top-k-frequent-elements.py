class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        # Step 3: Utilize Counter to get frequencies directly, simplifying the population of the `mp` dictionary.
        frequency_count = Counter(nums)

        # Step 4: Use the most_common method to get elements sorted by frequency.
        # No need for separate bucket sorting as Counter already provides frequencies sorted in descending order.
        most_common_elements = frequency_count.most_common()

        # Step 5: Collect the desired k elements directly from the sorted frequencies.
        ans = []
        for element, count in most_common_elements:
            ans.append(element)
            if len(ans) == k:
                break
        return ans
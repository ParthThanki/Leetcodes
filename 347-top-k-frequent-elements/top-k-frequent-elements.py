class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        # Utilizing Counter to efficiently count frequencies and extract the most common elements
        frequency_count = Counter(nums)

        # Since we only need the first k elements based on their frequency, we can directly access them
        # This step inherently sorts the elements by frequency in descending order and selects the top k.
        most_common_elements = frequency_count.most_common(k)

        # Extract just the elements (ignoring the counts) and print them
        ans = [element for element, count in most_common_elements]
        return ans
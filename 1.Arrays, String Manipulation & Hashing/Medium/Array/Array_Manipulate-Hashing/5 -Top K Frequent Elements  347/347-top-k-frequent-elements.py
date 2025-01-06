# Approach: Bucket Sort
# Time Complexity: 𝑂(𝑛)
# Space Complexity:𝑂(𝑛)


from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies
        freq_map = Counter(nums)

        # Step 2: Bucket sort by frequency
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in freq_map.items():
            bucket[freq].append(num)

        # Step 3: Collect top k frequent elements
        result = []
        for i in range(len(bucket) - 1, 0, -1):
            result.extend(bucket[i])
            if len(result) >= k:
                break

        return result[:k]

# THIS IS ALREADY A OPTIMAL SOLUTION SO DONT GO FOR OTHERS
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        # Step 1: Count frequencies
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        # Step 2: Sort the dictionary items by frequency
        sorted_freq = sorted(freq.items(), key=lambda x: x[1])

        # Step 3: Take the last k elements and return only the numbers
        result = []

        for i in range(len(sorted_freq) - k, len(sorted_freq)):
            result.append(sorted_freq[i][0])

        return result
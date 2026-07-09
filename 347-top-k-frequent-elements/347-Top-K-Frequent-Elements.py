# THIS IS A BETTER APPROACH WHICH USES HASHMAP + HEAP ( PRIORITY QUEUE)
import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Step 1: Create hashmap to store frequency
        frequency_map = {}

        # Count how many times each number appears
        for num in nums:

            if num not in frequency_map:
                frequency_map[num] = 1

            else:
                frequency_map[num] += 1


        # After this loop:
        # frequency_map = {
        #     1: 3,
        #     2: 2,
        #     3: 1
        # }


        # Step 2: Create an empty min heap
        min_heap = []


        # Step 3: Put every number with its frequency into heap
        for num in frequency_map:

            frequency = frequency_map[num]

            # Store (frequency, number)
            heapq.heappush(min_heap, (frequency, num))


            # If heap has more than k elements,
            # remove the element with smallest frequency
            if len(min_heap) > k:
                heapq.heappop(min_heap)



        # Step 4: Extract numbers from heap
        answer = []

        for frequency, num in min_heap:
            answer.append(num)


        return answer
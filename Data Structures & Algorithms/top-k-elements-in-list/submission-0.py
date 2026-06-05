from collections import Counter
import heapq 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        heap = []
        for value, freq in frequency.items():
            heapq.heappush(heap, (freq, value))  

            if len(heap) > k:
                heapq.heappop(heap)
        
        result = [res[1] for res in heap] 

        return result 

        
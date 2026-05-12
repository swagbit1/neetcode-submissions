import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for i in nums:
            d[i] = d.get(i, 0) + 1

        heap = []
        for number, count in d.items():
            heap.append((-1 * count,number))
        
        heapq.heapify(heap)

        result = []
        for i in range(k):
            count, number = heapq.heappop(heap)
            result.append(number)
        return result


import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        # count the elements
        for i in nums:
            d[i] = d.get(i, 0) + 1

        #build the heap using negative numbers
        # tuples compared left right
        # if count negative then lower so appears in front
        # heap prorety lowest in front
        # reverse means negative 1 * count to make big the lowest
        # and that is the largest in heap so reverse works
        heap = []
        for number, count in d.items():
            heap.append((-1 * count,number))
        
        # use heapify to build the heap
        heapq.heapify(heap)

        result = []
        # pop the heap and store tuple values and then append the number
        for i in range(k):
            count, number = heapq.heappop(heap)
            result.append(number)
        return result


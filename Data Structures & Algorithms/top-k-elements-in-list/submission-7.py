class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = {}

        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        res = []
        for i in range(k):
            pair = max(d.items(), key=lambda x: x[1])
            res.append(pair[0])
            del d[pair[0]]

        return res
       

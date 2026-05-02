class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        d = {}

        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        for key in d:
            if d[key] > 1:
                return True

        return False
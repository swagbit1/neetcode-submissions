class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # brute force

        for i,v in enumerate(nums):
            for j,v2 in enumerate(nums):
                if v + v2 == target and i != j:
                    return [i,j]
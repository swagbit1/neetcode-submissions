class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        products = []
        
        for index,value in enumerate(nums):
            curProduct = 1
            for index2, value2 in enumerate(nums):
                if index != index2:
                    curProduct *= value2
            products.append(curProduct)
        return products




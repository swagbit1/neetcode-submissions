class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        #[1,1,2,8],  i = 3, p = 48, does not run any more

        postfix = 1
        for i in range(len(nums) - 1, -1 ,-1):
            result[i] *= postfix
            postfix *= nums[i]
        #[48,24,12,8]. i = 0, p = 48, does not run more
        return result

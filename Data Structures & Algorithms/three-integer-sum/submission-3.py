class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # start with a sorted array
        res = []

        for i in range(len(nums)): # go through all the numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue # checking for same numbers, causes duplicates to occur

            l, r = i + 1, len(nums) - 1 # start l = i+1, since all the previous pairs will all be checked so going back is redundent
            target = -nums[i] # for the target we want n1 + n2 == target, so target should be negative

            while l < r: # two pointer method
                s = nums[l] + nums[r] # the sum of l and r

                if s < target: # checking and incrementing pointers based on closeness to target
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]]) # we know that these are equal 0 by condtions

                    l += 1 # move the pointers one more time
                    r -= 1

                    # ensure that the pointers dont cause duplicate values as well so move them until no more duplicates
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                    # and then check if there are more occurance (distinct) pairs that satisfy the condtion

        return res
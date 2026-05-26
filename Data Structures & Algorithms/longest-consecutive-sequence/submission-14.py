class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        #every sequuesnce (not) has a starting value ie 1,2,3 has start value 1
        # 1 does not have start so it is the first starting number
        # we check in set if such number exists by cheching if number has a starting value present
        # ie if we check to if 1 exists then 2 is not it so we move on
        # after finding this, we check if the ascending pattern exists in hash set
        # note that hash set has look up of 1 so its constant due to 
        # hash(x) converting it to a specific memoery so every look up is 1
        # after firnding a starting value, we just check the longest sequence and return

        for n in nums:
            if (n - 1) not in numSet:
                length = 0
                while (n + length ) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest
                
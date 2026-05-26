class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #brute force
        nums.sort()
        print(nums)
        counter = 0
        temp = 1
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i + 1] :
                temp += 1
            elif nums[i] == nums[i+1]:
                continue
            else:
                counter = max(temp,counter)
                temp = 1
        #[0, 1, 1, 2, 3, 4, 5, 6]
        # 0-7, i = 6, 2 +1 == 3 temp = 7
        if nums == []:
            return 0
        else:
            counter = max(temp,counter)

        return counter
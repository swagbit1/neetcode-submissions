class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #[4,3,5,6] target = 7
        # target - 3 = 4, we check if 4 in list or
        # in the event list not sorted, still works cuz
        # target - 4 = 3
        
        # 7 - 4 = 3, if 3 in d, return index of 4 and 3
        # else put index of 4 in d, continue
        # then 7 - 3 =4, 4 in d, return index of 4 and 3 done


        d = {}

        for index, value in enumerate(nums):
            number = target - value
            if number in d:
                return [d[number], index]
            else:
               d[value] = index 

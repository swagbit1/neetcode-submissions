class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # 1 2 3 4 5
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2

        print(left,right,mid)
        # l = 0, r = 5, mind = 2
        while(left <= right and nums[mid] != target ):
            print(nums)
            if target > nums[mid]:
                left = mid + 1

                # l =3 , mid =4 , r =5 
                # 
        
            if target < nums[mid]:
                right = mid - 1
            # l = 0, mid =0  , r = 1
            mid = (left + right) // 2

        
        if (nums[mid] == target):
            return mid
        else:
            return -1

        
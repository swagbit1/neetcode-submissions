class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for row in matrix:
            l = 0
            r = len(row) - 1
            
            while(l <= r):
                mid = (l + r) // 2

                if target > row[mid]:
                    l = mid + 1
                elif target < row[mid]:
                    r = mid - 1
                else:
                    return True
        
        return False
        
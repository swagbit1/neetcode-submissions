class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1

        while (l <= r):
            mid = (l + r) // 2

            row = matrix[mid]

            if (target >= row[0] and target <= row[-1]):
                l2 = 0
                r2 = len(row) - 1
                while (l2 <= r2):
                    mid2 = (l2 + r2) // 2
                    if target > row[mid2]:
                        l2 = mid2 + 1
                    elif target < row[mid2]:
                        r2 = mid2 - 1
                    else:
                        return True
                return False
            elif (target > row[-1]):
                l = mid + 1
            elif (target < row[0]):
                r = mid - 1
            
        return False
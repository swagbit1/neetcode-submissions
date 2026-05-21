class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]
        # this boxes works as a account to check if vals are inside the box
        # maps the boxes 3x3 form 0 - 8
        # and in each box checks if the val is already present

        for r in range(9):
            for c in range(9):

                val = board[r][c]

                if val == ".":
                    continue

                box = (r // 3) * 3 + (c//3)

                if val in rows[r]:
                    return False
                
                if val in cols[c]:
                    return False
                
                if val in boxes[box]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[box].add(val)
        return True

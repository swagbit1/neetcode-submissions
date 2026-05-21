class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # for i in board:
        #     print(i)
        # check if duplicates in cols
        for i in board:
            rows = set()
            for j in i:
                if j != "." and j in rows:
                    return False
                else:
                    rows.add(j)
        # check if duplicates in rows
        for j in range(len(board[0])):
            col = set()
            for i in range(len(board)):
                if board[i][j] != "." and board[i][j] in col:
                    print("fire2")

                    return False

                else:
                    col.add(board[i][j])

        # 3x3 squares
        #[1,2,3,4,5,6,7,8,9]
        # {0,1,2},{3,4,5},{6,7,8}
        for i in range(0,3): # start at 0 and move by 3
            for j in range(0,3):
                hashSquare = set()
                for r in range(i * 3,(i+1)*3):
                    for c in range(j*3,(j+1)*3):
                        cell = board[r][c]
                        print(i,j,i+r,j+c)
                        if cell != "." and cell in hashSquare:
                            # print("fire3",cell,i,j,r,c,i+r,j+c)
                            return False
                        else:
                            hashSquare.add(cell)
               
       
                
        return True

        
                



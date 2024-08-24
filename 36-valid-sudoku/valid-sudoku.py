class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for i in range(9):
            check = set()  # Use set for faster lookups
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in check:
                        print(1)  # Debugging output
                        return False
                    check.add(board[i][j])
        
        # Check columns
        for i in range(9):
            check = set()
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] in check:
                        print(2)  # Debugging output
                        return False
                    check.add(board[j][i])
        
        # Check 3x3 subgrids
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                check = set()
                for row in range(3):
                    for column in range(3):
                        cell = board[i + row][j + column]
                        if cell != ".":
                            if cell in check:
                                print(3)  # Debugging output
                                return False
                            check.add(cell)
        
        # If all checks pass, the board is valid
        return True
"""
For a valid sudoku board there's 3 constraints

vertical - traverse for up and down

horizontal - traverse left to right

box - set? - put all numbers in a set to make sure there's no duplicates


- validation function: no duplicates this makes me think set

3 separate methods for traversal


there are also empty vals so continue on those "."

"""




class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        vertical = collections.defaultdict(set)
        horizontal = collections.defaultdict(set)
        square = collections.defaultdict(set)



        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in horizontal[r] or 
                    board[r][c] in vertical[c] or 
                    board[r][c] in square[(r//3,c//3)]):
                    return False
                vertical[c].add(board[r][c])
                square[r//3,c//3].add(board[r][c])
                horizontal[r].add(board[r][c])
        return True


        
            
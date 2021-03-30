from typing import List
from enum import Enum

class Cell(Enum):
    ONE = "1"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    EMPTY = "."

class Sodoku: 
    LENGTH = 9

    def __init__(self, board: List[List[Cell]]):
        self.board = board

    def dfs(self, row: int, col: int) -> None:
        for i in range(row, self.LENGTH):
            for j in range(col, self.LENGTH):
                if (self.board[i][j] == Cell.EMPTY.value):
                    # Try to place 1-9 in the empty cell
                    for s in Cell:
                        t = s.value
                        if t not in board[i] and t not in self.getCol(j):
                            self.board[i][j] = t
                            self.dfs(i, j)
                            
                       


    def getCol(self, col: int) -> List[Cell]:
        return [row[col] for row in self.board]

    # This function can be called from anywhere
    # Call this function on some board that needs to be solved
    def solve(board: List[List[Cell]]) -> None:
        sodoku = Sodoku(board)

        for i in range(0, sodoku.LENGTH):
            for j in range(0, sodoku.LENGTH):
                col = sodoku.getCol(j)
                if (sodoku.board[i][j] == Cell.EMPTY.value):
                    for s in Cell:
                        t = s.value
                        if t not in board[i] and t not in col:
                            # Try this number
                            sodoku.board[i][j] = t
                            print(sodoku.board)
                            sodoku.dfs(i, j)



if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    Sodoku.solve(board)
    print(board)
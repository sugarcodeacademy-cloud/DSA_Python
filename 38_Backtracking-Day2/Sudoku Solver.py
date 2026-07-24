"""
Write a program to solve a Sudoku puzzle by filling the empty cells.
Empty cells are indicated by the character '.'
You may assume that there will be only one unique solution.
"""
# A=[[0,0,0,0],[0,3,2,4],[0,2,0,0],[4,0,3,2]]
A = [["53..7...."],
     ["6..195..."],
     [".98....6."],
     ["8...6...3"],
     ["4..8.3..1"],
     ["7...2...6"],
     [".6....28."],
     ["...419..5"],
     ["....8..79"]]
import math
class Solution:
    def check(self, puzzle, row, col, n, num):
        for j in range(n):
            if puzzle[row][j] == num: return False

        for i in range(n):
            if puzzle[i][col] == num: return False

        box_size = int(math.sqrt(n))
        start_row = (row//box_size)*box_size
        start_col = (col//box_size)*box_size

        for i in range(start_row, start_row + box_size):
            for j in range(start_col, start_col + box_size):
                if puzzle[i][j] == num:
                    return False

        return True

    def sudoku_solver(self, puzzle, n, row,col):
        if row == n:
            return True

        if col == n-1:
            next_row = row+1
            next_col = 0
        else:
            next_row = row
            next_col = col+1

        if puzzle[row][col] != ".":
                return self.sudoku_solver(puzzle,n, next_row, next_col)

        for num in map(str, range(1,n+1)):
            if self.check(puzzle, row, col, n, num):
                puzzle[row][col] = num

                if self.sudoku_solver(puzzle, n, next_row, next_col):
                    return True

                puzzle[row][col] = "."

        return False


    def solve(self, puzzle):
        for i in range(len(puzzle)):
            puzzle[i] = (list(puzzle[i][0]))
        if self.sudoku_solver(puzzle, len(puzzle), 0, 0):
            return puzzle
        return None


result = Solution().solve(A)
for row in result:
    print(row)





"""
The N-queens puzzle is the problem of placing N queens on an
N×N chessboard such that no two queens attack each other.
Given an integer A denoting the value of N, return all distinct solutions to the N-queens puzzle.
Each solution contains a distinct board configuration of the N-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
The final list should be generated in such a way that the indices of the queens in each list should be in reverse lexicographical order.
"""

A = 8
class Solution:
    def check(self, board, row, col, n):
        for i in range(0, row):
            if board[i][col] == "Q": return False

        x, y = row,col
        while x>0 and y>0:
            if board[x-1][y-1] == "Q": return False
            x -= 1
            y -= 1

        x,y = row, col
        while x >0 and y< n-1:
            if board[x-1][y+1] == "Q": return False
            x -= 1
            y += 1

        return True


    def n_queens(self, board, n, row, res):
        if row == n:
            return res.append([["".join(row[:])]for row in board])


        for col in range(n):
            if self.check(board, row, col , n):
                board[row][col] = "Q"
                self.n_queens(board, n, row+1, res)
                board[row][col] = "."

    def solve(self, size):
        board = [["." for _ in range(size)]for _ in range(size)]
        result = []
        self.n_queens(board, size, 0, result)
        return result


print(Solution().solve(4))




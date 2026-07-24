"""
Problem: Rat in a Maze

A rat is placed at the top-left corner (0, 0) of an N × N maze represented by a binary matrix.

A cell containing 1 represents an open path that the rat can move through.
A cell containing 0 represents a blocked cell that the rat cannot enter.

The rat's goal is to reach the bottom-right corner (N-1, N-1).

The rat can move only in the following four directions:

U → Up
D → Down
L → Left
R → Right

A cell cannot be visited more than once in the same path.

Return all possible paths from the start to the destination. Each path should be represented as a string consisting of the characters U, D, L, and R.

If no valid path exists, return an empty list.
"""
maze = [[1,1,0,0],
        [1,1,1,0],
        [0,0,1,0],
        [1,1,1,1]]

maze_failure=[[1,1,1,0],
              [1,0,1,0],
              [0,1,1,0],
              [0,1,0,1]]

def solve(maze):
    n = len(maze)

    if maze[0][0] == 0 or maze[n-1][n-1] == 0:
        return []

    visited = [[False]*n for _ in range(n)]

    result = []

    rat_in_maze(maze, 0, 0, n, visited,"", result)
    return result

def rat_in_maze(maze, row, col, n, visited, path, res):
    #Base case
    if row == n-1 and col == n-1:
        res.append(path)
        return

    visited[row][col] = True

    # Down
    if row+1 < n and maze[row+1][col] == 1 and not visited[row+1][col]:
        rat_in_maze(maze, row+1, col, n, visited, path+"D", res)

    # Right
    if col+1 < n and maze[row][col+1] == 1 and not visited[row][col+1]:
        rat_in_maze(maze, row, col+1, n , visited, path+"R", res)

    # Up
    if row - 1 >= 0 and maze[row - 1][col] == 1 and not visited[row - 1][col]:
        rat_in_maze(maze, row - 1, col, n, visited, path +"U", res)

    # Left
    if col-1 >= 0 and maze[row][col-1] == 1 and not visited[row][col-1]:
        rat_in_maze(maze, row, col-1, n , visited, path+"L", res)

    visited[row][col] = False

print(solve(maze_failure))

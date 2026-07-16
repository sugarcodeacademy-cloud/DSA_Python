"""
Given a binary mat[N][M], find no. of distinct rows
"""

mat =[[1,0,0,1,0],
      [1,1,0,1,1],
      [0,1,0,1,0],
      [1,1,0,1,1],
      [1,1,0,0,1],
      [1,0,0,1,0],
      [0,0,1,1,0]]

class TrieNode:
    def __init__(self):
        self.children = [None, None]

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, arr, M):
        temp = self.root
        flag = False
        for i in range(M):
            element = arr[i]
            if temp.children[element] is None:
                temp.children[element] = TrieNode()
                flag = True
            temp = temp.children[element]
        return flag

def unique_rows(matrix):
    N = len(mat)
    M = len(mat[0])
    trie = Trie()
    count = 0
    for i in range(N):
        if trie.insert(mat[i],M):
            count += 1
    return count

print(unique_rows(mat))

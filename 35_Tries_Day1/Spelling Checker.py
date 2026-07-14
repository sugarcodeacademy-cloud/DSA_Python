"""
Given an array of words A (dictionary) and another array B (which contain some words).
You have to return the binary array (of length |B|) as the answer where 1 denotes that the word is present in the dictionary and 0 denotes it is not present.
Formally, for each word in B, you need to return 1 if it is present in Dictionary and 0 if not.
Such problems can be seen in real life when we work on any online editor (like Google Documnet), if the word is not valid it is underlined by a red line.
"""
A = [ "hat", "cat", "rat" ]
B = [ "cat", "ball" ]
class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True

    def search(self, word: str):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
        return node.isEnd

class Solution:
    def solve(self, A, B):
        result = []
        trie_node = Trie()
        for word in A:
            trie_node.insert(word)
        for search_word in B:
            result.append(int(trie_node.search(search_word)))
        return result

obj = Solution()
print(obj.solve(A, B))
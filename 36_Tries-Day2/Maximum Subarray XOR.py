"""
Given an array of size N, Find the maximum subarray XOR
"""

A=[3,8,2]

class TrieNode:
    def __init__(self):
        self.children = [None, None]

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        temp = self.root
        for i in range(31, -1, -1): #start from the most important bit i.e., 2^32
            bit = (num >> i) & 1 #get the current bit value
            #check if the node for bit is present, if not create a node and traverse else only traverse
            if temp.children[bit] is None:
                temp.children[bit] = TrieNode()
            #traverse is common irrespective of if node for bit is present or not
            temp = temp.children[bit]

    def max_xor(self, num):
        temp = self.root
        ans = 0
        for i in range(31, -1, - 1):  # start from the most important bit i.e., 2^32
            bit = (num >> i) & 1 #get the current bit value
            opposite = 1 - bit #get the opposite of current bit
            #check for opposite as opposite bit gives the maximum xor value
            if temp.children[opposite] is not None:
                temp = temp.children[opposite] #traverse on the opposite side
                # since bot bits are opposite, xor value is 1, so insert 1 at the current bit position in the ans
                ans = ans | (1<<i)
            else:
                temp = temp.children[bit] #traverse on the same side, xor value of same bit is zero so no changes in ans
        return ans #return the max_xor value with all values on the left in the prefix array

def max_subarray_XOR(arr):
        trie = Trie() #creates a new Trie object
        result = 0
        trie.insert(0) #since prefix array first value is always zero
        prefix = 0
        for num in arr:
            prefix = prefix ^ num # carry forward the prefix
            result = max(result, trie.max_xor(prefix))
            trie.insert(prefix)
        return result

print(max_subarray_XOR(A))





"""
Implement a Min Heap from scratch.

Design a data structure that supports the following operations efficiently:

insert(x) – Insert an element into the heap.
deleteMin() – Remove and return the minimum element.
getMin() – Return the minimum element without removing it.
size() – Return the number of elements in the heap.
isEmpty() – Return whether the heap is empty.
"""
class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, child_idx):
        return (child_idx-1)//2

    def left(self, parent_idx):
        return 2*parent_idx+1

    def right(self, parent_idx):
        return 2*parent_idx+2

    def insert(self,heap,ele):
        self.heap.append(ele)
        ele_index = self.size()-1
        parent_idx = self.parent(ele_index)
        while ele_index != 0 and self.heap[parent_idx] > self.heap[ele_index]:
            self.heap[parent_idx], self.heap[ele_index] = self.heap[ele_index], self.heap[parent_idx]
            ele_index = parent_idx
            parent_idx = self.parent(ele_index)

    def get_min(self):
        return self.heap[0]

    def delete_min(self):
        if not self.isEmpty():
            self.heap[0], self.heap[self.size()-1] = self.heap[self.size()-1], self.heap[0]
            min_value = self.heap.pop()
            ele_idx = 0
            min_index = min(self.heap[self.left(ele_idx)], self.heap[self.right(ele_idx)])
            while (self.left(ele_idx) < self.size() and self.right(ele_idx) < self.size() and
                   self.heap[ele_idx] > self.heap[min_index]):
                self.heap[ele_idx], self.heap[min_index] = self.heap[min_index], self.heap[ele_idx]
                ele_idx = min_index
                min_index = min(self.heap[self.left(ele_idx)], self.heap[self.right(ele_idx)])
            return min_value

    def size(self):
        return len(self.heap)

    def isEmpty(self):
        return len(self.heap) == 0





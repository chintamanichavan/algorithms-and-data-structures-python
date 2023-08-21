import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, value):
        heapq.heappush(self.heap, value)

    def pop(self):
        return heapq.heappop(self.heap)

    def peek(self):
        return self.heap[0]

    def __len__(self):
        return len(self.heap)

class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, value):
        heapq.heappush(self.heap, -value)  # Negate values to simulate a max heap

    def pop(self):
        return -heapq.heappop(self.heap)  # Negate again to retrieve the original value

    def peek(self):
        return -self.heap[0]

    def __len__(self):
        return len(self.heap)

# Example usage
min_heap = MinHeap()
min_heap.push(5)
min_heap.push(3)
min_heap.push(7)
print(min_heap.peek())  # Output: 3
print(min_heap.pop())   # Output: 3

max_heap = MaxHeap()
max_heap.push(5)
max_heap.push(3)
max_heap.push(7)
print(max_heap.peek())  # Output: 7
print(max_heap.pop())   # Output: 7

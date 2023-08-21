import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.counter = 0  # Used to handle equal priorities

    def push(self, item, priority):
        heapq.heappush(self.heap, (priority, self.counter, item))
        self.counter += 1

    def pop(self):
        return heapq.heappop(self.heap)[-1]

    def peek(self):
        return self.heap[0][-1]

    def __len__(self):
        return len(self.heap)

# Example usage
pq = PriorityQueue()
pq.push("Task 1", 3)
pq.push("Task 2", 1)
pq.push("Task 3", 2)

print(pq.peek())  # Output: "Task 2"
print(pq.pop())   # Output: "Task 2"

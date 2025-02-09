class NumberContainers:

    def __init__(self):
        self.number_to_idx = {}  # Maps numbers to a sorted set of indices
        self.idx_to_number = {}  # Maps indices to numbers


    def change(self, index: int, number: int) -> None:
        self.idx_to_number[index] = number  # O(1)
        if number not in self.number_to_idx:
            self.number_to_idx[number] = []
        heapq.heappush(self.number_to_idx[number], index)
    
    
    def find(self, number: int) -> int:
        if number not in self.number_to_idx:
            return -1

        pq = self.number_to_idx[number]
        while pq:
            idx = pq[0]  # O(1)
            if self.idx_to_number.get(idx) == number:
                return idx
            heapq.heappop(pq)  # O(log n)
        return -1

        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
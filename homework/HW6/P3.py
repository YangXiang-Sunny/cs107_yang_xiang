from P2 import MinHeap
from heapq import *


class PriorityQueue:
    def __init__(self, max_size):
        self.elements = []
        self.max_size = max_size

    def __len__(self):
        return len(self.elements)

    def __bool__(self):
        return len(self.elements) > 0

    def put(self, val):
        raise NotImplementedError # TODO

    def get(self):
        raise NotImplementedError # TODO

    def peek(self):
        raise NotImplementedError # TODO


class NaivePriorityQueue(PriorityQueue):
    def put(self, val):
        if self.max_size == len(self.elements):
            raise IndexError
        self.elements.append(val)

    def get(self):
        if not self.elements:
            raise IndexError
        min_val = None
        min_idx = None
        for i in range(len(self.elements)):
            if (min_val is None) or (self.elements[i] < min_val):
                min_val = self.elements[i]
                min_idx = i
        del self.elements[min_idx]
        return min_val

    def peek(self):
        if not self.elements:
            raise IndexError
        min_val = None
        for i in range(len(self.elements)):
            if (min_val is None) or (self.elements[i] < min_val):
                min_val = self.elements[i]
        return min_val


class HeapPriorityQueue(MinHeap):
    def __init__(self, max_size):
        self.elements = []
        self.max_size = max_size
        self.size = 0

    def put(self, val):
        if self.max_size == len(self.elements):
            raise IndexError
        self.heappush(val)

    def get(self):
        if not self.elements:
            raise IndexError
        return self.heappop()

    def peek(self):
        if not self.elements:
            raise IndexError
        return self.elements[0]


class PythonHeapPriorityQueue(PriorityQueue):
    def put(self, val):
        if self.max_size == len(self.elements):
            raise IndexError
        heappush(self.elements, val)

    def get(self):
        if not self.elements:
            raise IndexError
        return heappop(self.elements)

    def peek(self):
        if not self.elements:
            raise IndexError
        return self.elements[0]



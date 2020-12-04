from math import floor
from typing import List


class Heap:
    def __init__(self, array: List[int]) -> None:
        self.elements = array
        self.size = len(array) # Number of elements in heap
        self.build_heap()

    # index of left child of the node at idx
    def left(self, idx: int) -> int:
        return 2 * idx + 1

    # index of right child of the node at idx
    def right(self, idx: int) -> int:
        return 2 * idx + 2

    def parent(self, idx: int) -> int:
        return floor((idx - 1) / 2)

    def swap(self, idx1: int, idx2: int) -> None:
        tmp = self.elements[idx1]
        self.elements[idx1] = self.elements[idx2]
        self.elements[idx2] = tmp

    def to_string(self, prefix: str = "", idx: int = 0, left: bool = False) -> str:
        if self.size == 0:
            return '\\--'
        elif idx < self.size:
            buf = prefix
            if left:
                buf = buf + "|-- "
            else:
                buf = buf + "\\-- "
            buf = buf + '\033[1m' + str(self.elements[idx]) + '\033[0m' + '\n'
            #buf = buf + str(self.elements[idx]) + '\n' #use if above doesn't work

            new_prefix = prefix
            if left:
                new_prefix = new_prefix + "|   "
            else:
                new_prefix = new_prefix + "    "

            return buf + \
                    self.to_string(new_prefix, self.left(idx), True) + \
                    self.to_string(new_prefix, self.right(idx), False)
        else:
            return ''

    def __str__(self) -> str:
        return self.to_string()

    def __len__(self) -> int:
        return self.size

    # TODO: override this in your dervied classes
    def compare(self, a: int, b: int) -> bool:
        raise NotImplementedError

    def heapify(self, idx: int) -> None:
        idx_left = self.left(idx)
        idx_right = self.right(idx)

        if idx_left >= self.size:
            # Node has no children
            return

        if idx_right >= self.size:
            # Node has only left child
            if self.compare(self.elements[idx], self.elements[idx_left]):
                self.swap(idx, idx_left)
                return
            else:
                return

        if (self.compare(self.elements[idx], self.elements[idx_left])) or \
                (self.compare(self.elements[idx], self.elements[idx_right])):
            if self.compare(self.elements[idx_left], self.elements[idx_right]):
                self.swap(idx, idx_right)
                self.heapify(idx_right)
            else:
                self.swap(idx, idx_left)
                self.heapify(idx_left)
        else:
            return

    def build_heap(self) -> None:
        for i in range(floor(self.size / 2.0) - 1, -1, -1):
            self.heapify(i)

    def heappush(self, key: int) -> None:
        self.elements.append(key)
        self.size += 1

        idx = self.size - 1
        idx_parent = self.parent(idx)

        while self.compare(self.elements[idx_parent], self.elements[idx]):
            # Swap current key and parent key
            self.swap(idx, idx_parent)
            # Update index to parent
            idx = idx_parent
            idx_parent = self.parent(idx_parent)
            # Break if hit the root node
            if idx == 0:
                break

    def heappop(self) -> int:
        if self.size == 0:
            raise IndexError

        self.swap(0, self.size - 1)
        key_pop = self.elements.pop()
        self.size -= 1
        # Heapify the new root key
        self.heapify(0)

        return key_pop


class MinHeap(Heap):
    def compare(self, a: int, b: int) -> bool:
        return a > b


class MaxHeap(Heap):
    def compare(self, a: int, b: int) -> bool:
        return a < b


# if __name__ == "__main__":
#     mn = MinHeap([1, 2, 3, 4, 5])
#     mx = MaxHeap([1, 2, 3, 4, 5])
#     print(mn)
#     print(mx)
#
#     mn.heappop()
#     mx.heappop()
#     print(mn)
#     print(mx)
#
#     mn.heappush(0)
#     mx.heappush(3)
#     print(mn)
#     print(mx)


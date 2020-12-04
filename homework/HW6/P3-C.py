from P3 import PythonHeapPriorityQueue, HeapPriorityQueue, NaivePriorityQueue, PriorityQueue
from time import time
from random import sample
import matplotlib.pyplot as plt


def mergesortedlists(lists, pqclass=PriorityQueue):
    merged = []
    pq = pqclass(len(lists))
    for i, l in enumerate(lists):
        pq.put((l.pop(0), i))

    while pq:
        ele, i = pq.get()
        merged.append(ele)
        if lists[i]:
            pq.put((lists[i].pop(0), i))

    return merged


def generatelists(n, length=20, dictionary_path='./words.txt'):
    with open(dictionary_path, 'r') as f:
        words = [w.strip() for w in f.readlines()]
    lists = []
    for _ in range(n):
        lists.append(sorted(sample(words, length)))
    return lists


def timeit(ns=(10, 20, 50, 100, 200, 500), pqclass=PriorityQueue, n_average=5):
    elapsed = []
    for n in ns:
        timeaccum = 0
        for _ in range(n_average):
            lists = generatelists(n)
            start = time()
            merged = mergesortedlists(lists, pqclass)
            end   = time()
            timeaccum += end-start
        elapsed.append(timeaccum / n_average)
    return elapsed


ns = (10, 20, 50, 100, 200, 500)
time_NaivePriorityQueue = timeit(ns, NaivePriorityQueue)
time_HeapPriorityQueue = timeit(ns, HeapPriorityQueue)
time_PythonHeapPriorityQueue = timeit(ns, PythonHeapPriorityQueue)

plt.figure(figsize=(8, 8))
plt.plot(ns, time_NaivePriorityQueue, label="NaivePriorityQueue")
plt.plot(ns, time_HeapPriorityQueue, label="HeapPriorityQueue")
plt.plot(ns, time_PythonHeapPriorityQueue, label="PythonHeapPriorityQueue")
plt.xlabel("Number of Lists")
plt.ylabel("Average Time Elapsed")
plt.title("Compare Running Time of Different Priority Queue")
plt.legend()
plt.show()
# plt.savefig("./P3-C.png")


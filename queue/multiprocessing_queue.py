from multiprocessing import Queue

customQueue = Queue(maxsize=3)
customQueue.put(3)
customQueue.put(2)
print(customQueue.get())

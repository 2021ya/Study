import queue

# 创建队列queue
q = queue.Queue()

# 存放数据-----先进先出
q.put("a") # 可存放任意数据
q.put(1)
q.put({"name": "a", "age": 23})

# 取数据-----FIFO(first in first out)
print(q.get())
print(q.get())
print(q.get())
# print(q.get())  # 若未有数据，此处会堵塞，直到有新数据

# ——————————————————————————————————————————————————————————————————————————————————

# 创建堆栈queue-----lIFO(last in first out)先进后出，类似于电梯
lifoq = queue.LifoQueue()

lifoq.put("a")
lifoq.put(1)
lifoq.put({"name": "a", "age": 23})

print(lifoq.get())
print(lifoq.get())
print(lifoq.get())

# ————————————————————————————————————————————————————————————————————————————————————

# 创建优先级queue
priorityq = queue.PriorityQueue()

# 传入元组，第一个为优先级，数字越小，优先级越高，第二个为数据
priorityq.put((10, "data"))
priorityq.put((30, 2))
priorityq.put((20, {"data2": 12313}))

print(priorityq.get())
print(priorityq.get())
print(priorityq.get())

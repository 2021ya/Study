import multiprocessing


q = multiprocessing.Queue(3)  # 此处括号可写数字，意味着是否限制数据数量，此处的queue和线程的queue相同，但是这个是进程直接的queue

q.put(1)
q.put(2)
q.put(3)

try:
    q.put(4, timeout=2)  # timeout为等待时间,如果时间到了会异常

except Exception as e:
    print(e)

try:
    q.put_nowait(4)  # 不等直接放
except Exception as e:
    print(e)

print(q.full())  # 判断是否满数据

if not q.empty():  # empty是判断是否为空
    print(q.get())
    q.get_nowait()  # 不等，直接拿，如果没有数据会一直等待，直到有数据


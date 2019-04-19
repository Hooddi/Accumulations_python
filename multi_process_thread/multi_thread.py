# -*- coding: utf-8 -*-
'''
@ author      : Di Hu
@ contact     : hudi_0011@yeah.net
@ date        : 2019/4/1 15:36
@ file        : multi_thread.py
@ description : python中多线程实现方式，包括带返回值的实现
'''
import threading, time


def sum(n):
    print(threading.current_thread())
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i
        time.sleep(0.001)

    return sum


# ------------------------单线程-----------------------------------
time1 = time.time()
sum(1000)
sum(1000)
interval1 = time.time() - time1
print('interval: %.4f' % interval1)

# -------------------多线程，不带返回值----------------------------
n = [1000, 1000]
mythread = []
time2 = time.time()
for i in range(len(n)):
    t = threading.Thread(target=sum, args=(n[i],))
    mythread.append(t)
for i in range(len(n)):
    mythread[i].start()

for i in range(len(n)):
    mythread[i].join()

interval2 = time.time() - time2
print('interval: %.4f' % interval2)
print("cost:", time.time() - time2)
print(threading.current_thread())


# --------------------多线程，带返回值----------------------------
class Mythread(threading.Thread):
    def __init__(self, fun, args):
        threading.Thread.__init__(self)
        self.fun = fun
        self.args = args

    def run(self):
        self.result = self.fun(*self.args)

    def get_result(self):
        try:
            return self.result
        except Exception:
            return None


n = [1000, 1000]
my = []
time3 = time.time()

for i in range(len(n)):
    t = Mythread(sum, (n[i],))
    my.append(t)
    my[i].start()

res = []
for i in range(len(n)):
    my[i].join()
    res.append(my[i].get_result())

interval3 = time.time() - time3
print('interval: %.4f' % interval3)
print("cost:", time.time() - time3)
print(threading.current_thread())

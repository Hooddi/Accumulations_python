# -*- coding: utf-8 -*-
'''
@ author      : Di Hu
@ contact     : hudi_0011@yeah.net
@ date        : 2019/4/1 15:23
@ file        : multi_processing.py
@ description : python中多进程实现方式，包括带返回值的实现
'''
from multiprocessing import Pool, Manager, Process
import os, time


# --------------------------函数没有返回结果，只执行打印，指定pool大小
def sum_1(n):
    print('Run task %s ' % os.getpid())
    sum = 0
    for i in range(1, n + 1):
        sum += i
        time.sleep(0.001)
    print('前 %d 个数相加等于：%d' % (n, sum))


if __name__ == '__main__':
    p = Pool(4)
    for i in range(5):
        p.apply_async(sum_1, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')


# --------------------------保存返回结果，不指定pool大小
def sum_2(n, res_list):
    print('Run task %s ' % os.getpid())
    sum = 0
    for i in range(1, n + 1):
        sum += i
        time.sleep(0.001)
    res_list.append(sum)


if __name__ == '__main__':
    manager = Manager()
    res_list = manager.list()  # 结果保存在res_list中， 也可以保存成res_dict=manager.dict()
    for i in range(5):
        p = Process(target=sum_2, args=(i, res_list))
        p.start()
        p.join()

    print(res_list)
# res_list[i]


# --------------------------保存返回结果，指定pool大小
def sum_3(n):
    print('Run task %s ' % os.getpid())
    sum = 0
    for i in range(1, n + 1):
        sum += i
        time.sleep(0.001)
    # return_list.append(sum)
    return sum


if __name__ == '__main__':
    results = []
    p = Pool(3)
    for i in range(5):
        results.append(p.apply_async(sum_3, args=(i,)))
    p.close()
    p.join()
# results[0]._value

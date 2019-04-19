# -*- coding: utf-8 -*-
'''
@ author      : Di Hu
@ contact     : hudi_0011@yeah.net
@ date        : 2019/4/1 15:43
@ file        : time_example.py
@ description : python中关于time模块的使用
'''
import time

# ----获取系统当前时间
t1 = time.time()  # 返回当前时间的时间戳，float类型

# ----时间戳与struct_time相互转换
t2 = time.localtime(t1)  # 接收时间戳,返回struct_time
t3 = time.mktime(t2)  # 接收struct_time,返回时间戳int()

# ----时间的字符串形式
t4 = time.asctime(t2)  # 接受struct_time并返回一个可读的形式：'Mon Apr  1 15:53:15 2019'，str类型
t5 = time.asctime()  # 若不传入参数，表明返回当前时刻的可读形式
t6 = time.ctime(t1)  # 接收时间戳并返回一个可读的形式：'Mon Apr  1 15:53:15 2019'，str类型
t7 = time.ctime()  # 若不传入参数，表明返回当前时刻的可读形式

# ----将struct_time转换成规定格式的时间字符串
t8 = time.strftime('%Y-%m-%d %H:%M:%S', t2)  # 接收一个struct_time，返回'%Y-%m-%d %H:%M:%S'格式的时间字符串
t9 = time.strftime('%Y-%m-%d %H:%M:%S')  # 若不传入struct_time, 返回当前时刻的'%Y-%m-%d %H:%M:%S'格式的时间字符串

# ----将成规定格式的时间字符串转换成struct_time
t10 = time.strptime(t7, '%Y-%m-%d %H:%M:%S')  # .strftime()的逆操作，接收规定格式的时间字符串返回struct_time

# ----推迟线程运行，sleep
time.sleep(0.001)  # 单位是：s

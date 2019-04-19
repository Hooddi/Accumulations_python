# -*- coding: utf-8 -*-
'''
@ author      : Di Hu
@ contact     : hudi_0011@yeah.net
@ date        : 2019/4/1 16:46
@ file        : datetime_example.py
@ description : python中关于datetime模块的使用
'''
import datetime, time

# -----datetime.date类(year,month,day)
t0 = time.time()
t1 = datetime.date(2019, 4, 1)  # 接收一个tuple(year,month,day), 返回一个datetime.data对象（实例）
t2 = datetime.date(2019, 4, 1).ctime()  # 返回日期的可读形式：'Mon Apr  1 00:00:00 2019'，参考time, str类型
t3 = datetime.date(2019, 4, 1).timetuple()  # 返回struct_time对象
t4 = datetime.date(2019, 4, 1).strftime('%Y-%m-%d')  # 返回规定格式的时间字符串，str类型
t5 = datetime.date.fromtimestamp(t0)  # 接收时间戳，返回一个datetime.data对象（实例）
t6 = datetime.date(2019, 4, 1).isoweekday()  # 返回指定日期的星期（1-7）， 星期一=1，星期日=7
t7 = datetime.date(2019, 4, 1).weekday()  # 返回日期的星期，星期一=0，星期日=6

# -----datetime.datetime类(year, month, day, hour, minute, second, microsecond)可以扩展
t8 = datetime.datetime(2019, 4, 1, 17, 21, 35)  # 返回一个datetime.datetime对象
t9 = datetime.datetime.now()  # 返回系统当前时间，datetime.datetime对象
t10 = datetime.datetime.now().date()  # 返回系统当前时间，日期部分datetime.date对象
t11 = datetime.datetime.now().time()  # 返回系统当前时间，时间部分datetime.time对象
t12 = datetime.datetime(2019, 4, 1, 17, 21, 35).ctime()  # 返回日期+时间的可读形式：'Mon Apr  1 00:00:00 2019'，参考time, str类型
t13 = datetime.datetime(2019, 4, 1, 17, 21, 35).strftime('%Y-%m-%d %H:%M:%S')  # 返回规定格式的时间字符串，str类型

# -----datetime.time类(hour,minute,second,microsecond,tzoninfo)
t14 = datetime.time(20, 46, 35)  # 接收tuple(hour,minute,second), 返回一个datetime.time对象（实例）
t15 = datetime.time(20, 46, 35).strftime('%H:%M:%S')  # 返回规定格式的时间字符串，str类型
t16 = datetime.time(20, 46, 35).isoformat()

# -----datetime.timedelta类,两个datetime对象可以相加减(同为datetime类或者time类或者date类)
t17 = datetime.timedelta(0, 8, 732000)  # 表示一个datetime.timedelta类
t18 = datetime.timedelta(0, 8, 732000).seconds  # 返回该时间差转换成seconds的大小
t19 = datetime.timedelta(200).days

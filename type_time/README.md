主要是time模块和datetime模块的使用,以及考虑代码执行效率会用到timeit模块

time模块中，三种时间表现形式：
timestamp：时间戳，时间戳表示的是从1970年1月1日00:00:00开始按秒计算的偏移量。
struct_time： 时间元组，共有九个元素组。
format time： 格式化时间，已格式化的结构使时间更具可读性。包括自定义格式和固定格式。场指时间格式字符串


datetime模块中定义了5个类：
datetime.date：表示日期的类
datetime.datetime：表示日期时间的类
datetime.time：表示时间的类
datetime.timedelta：表示时间间隔，即两个时间点的间隔
datetime.tzinfo：时区的相关信息




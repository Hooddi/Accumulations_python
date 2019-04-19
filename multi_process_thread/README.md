1.多进程：适用于CPU密集型任务，比如大数量的计算等。
2.多线程：适用于IO密集型任务，比如网络爬虫等。
3.一个任务包含一个以上进程，一个进程包含一个以上线程。
4.对于计算量大的任务采用多线程并不会提高速度，因为多个线程共用进程资源。


python中多进程实现：multiprocessing (python3 中自带)
python中多线程实现：threading（python3 中自带）



concurrent.futures
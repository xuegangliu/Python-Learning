# Python线程
Python中使用线程有两种方式：函数或者用类来包装线程对象。

## 函数式：调用 _thread 模块中的start_new_thread()函数来产生新线程。
'''_thread.start_new_thread ( function, args[, kwargs] )'''
参数说明:
* function - 线程函数。
* args - 传递给线程函数的参数,他必须是个tuple类型。
* kwargs - 可选参数。

* _thread 提供了低级别的、原始的线程以及一个简单的锁，它相比于 threading 模块的功能还是比较有限的。
* threading 模块除了包含 _thread 模块中的所有方法外，还提供的其他方法：
* threading.currentThread(): 返回当前的线程变量。
* threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
* threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。
## 除了使用方法外，线程模块同样提供了Thread类来处理线程，Thread类提供了以下方法:
* run(): 用以表示线程活动的方法。
* start():启动线程活动。
* join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
* isAlive(): 返回线程是否活动的。
* getName(): 返回线程名。
* setName(): 设置线程名。

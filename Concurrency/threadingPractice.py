# from threading import Thread
# from threading import current_thread

# def thread_task(a, b, c, key1, key2):
#     print("{0} received the arguments: {1} {2} {3} {4} {5}".format(current_thread().getName(), a, b, c, key1, key2))

# myThread = Thread(group=None,  # reserved
#                   target=thread_task,  # callable object
#                   name="demoThread",  # name of thread
#                   args=(1, 2, 3),  # arguments passed to the target
#                   kwargs={'key1': 777,
#                           'key2': 111},  # dictionary of keyword arguments
#                   daemon=None  # set true to make the thread a daemon
#                   )

# myThread.start()  # start the thread

# myThread.join()  # wait for the thread to complete


from threading import Thread
from threading import current_thread


# class MyTask(Thread):

#     def __init__(self):
#         # The two args will not get passed to the overridden
#         # run method.
#         Thread.__init__(self, name="subclassThread", args=(2, 3))

#     def run(self):
#         print("{0} is executing".format(current_thread().getName()))


# myTask = MyTask()

# myTask.start()  # start the thread

# myTask.join()  # wait for the thread to complete

# print("{0} exiting".format(current_thread().getName()))


class MyThread(Thread):
    def __init__(self):
        Thread.__init__(self, name="demoThread", args=(1,2))

    def run(self):
        print("{0} is executing".format(current_thread().getName()))

obj = MyThread()
obj.start()
obj.join()
print("{0} exiting".format(current_thread().getName()))
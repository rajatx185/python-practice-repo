"""
Pseudo code
void increment() {
    acquire MUTEX_A
    acquire MUTEX_B
    //do work
    release MUTEX_B
    release MUTEX_A
}


void decrement(){
  acquire MUTEX_B
  acquire MUTEX_A
    // do work here
  release MUTEX_A
  release MUTEX_B
}

The above code can potentially result in a deadlock. Note that deadlock may not always happen, but for certain execution sequences, deadlock can occur. Consider the execution sequence below that ends up in a deadlock:

T1 enters function increment
T1 acquires MUTEX_A
T1 gets context switched by the operating system
T2 enters function decrement
T2 acquires MUTEX_B
both threads are blocked now

Thread T2 can't make progress as it requires MUTEX_A which is being held by T1. Now when T1 wakes up, it can't make progress as it requires MUTEX_B and that is being held up by T2. This is a classic text-book example of a deadlock.
"""

from threading import *
import time

def thread_A(lock1, lock2):
    lock1.acquire()
    print("{0} acquired lock1".format(current_thread().getName()))
    time.sleep(1)
    lock2.acquire()
    print("{0} acquired both locks".format(current_thread().getName()))


def thread_B(lock1, lock2):
    lock2.acquire()
    print("{0} acquired lock2".format(current_thread().getName()))
    time.sleep(1)
    lock1.acquire()
    print("{0} acquired both locks".format(current_thread().getName()))


if __name__ == "__main__":

    lock1 = Lock()
    lock2 = Lock()

    Thread(target=thread_A, args=(lock1, lock2)).start()
    Thread(target=thread_B, args=(lock1, lock2)).start()
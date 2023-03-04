"""
Consider the snippet below. We have two threads working on the same variable rand_int. The modifier thread perpetually updates the value of rand_int in a loop while the printer thread prints the value of rand_int only if rand_int is divisible by 5. If you let this program run, you'll notice some values get printed even though they aren't divisible by 5 demonstrating a thread-unsafe version of test-then-act.

"""

from threading import *
import random
import time

rand_int = 0


def updater():
    global rand_int
    while 1:
        rand_int = random.randint(1, 9)


def printer():
    global rand_int
    while 1:    
        # test
        if rand_int % 5 == 0:
            # if rand_int % 5 != 0:
                # and act
                print(rand_int)


if __name__ == "__main__":
    Thread(target=updater, daemon=True).start()
    Thread(target=printer, daemon=True).start()

    # Let the simulation run for 5 seconds
    time.sleep(5)

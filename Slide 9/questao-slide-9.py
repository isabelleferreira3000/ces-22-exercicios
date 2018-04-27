# Processes vs. Threads: Advantages and Disadvantages
#
# Process
#     Processes are heavyweight operations
#     Each process has its own memory space
#     Inter-process communication is slow as processes have different memory addresses
#     Context switching between processes is more expensive
#     Processes don’t share memory with other processes
#
# Thread
#     Threads are lighter weight operations
#     Threads use the memory of the process they belong to
#     Inter-thread communication can be faster than inter-process communication because threads of the same process
#         share memory with the process they belong to
#     Context switching between threads of the same process is less expensive
#     Threads share memory with other threads of the same process


import multiprocessing
from threading import Thread
import sys
import time

COUNTDOWN = 5


class Th(Thread):

    def __init__ (self, num):
        sys.stdout.write("Making thread number " + str(num) + "n")
        sys.stdout.flush()
        Thread.__init__(self)
        self.num = num
        self.countdown = COUNTDOWN

    def run(self):

        while self.countdown:
            sys.stdout.write("Thread " + str(self.num) + " (" + str(self.countdown) + ")\n")
            sys.stdout.flush()
            self.countdown -= 1


def worker():
    """worker function"""
    print('Worker')
    return


if __name__ == '__main__':
    jobs = []
    t0 = time.time()
    for i in range(5):
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()
    t1 = time.time()

    # t2 = time.time()
    for thread_number in range(5):
        thread = Th(thread_number)
        thread.start()

    t2 = time.time()

    # As vezes processamento leva mais tempo que thread, as vezes é o contrário
    print("tempo do Multiprocessamento: " + str(t1-t0))  # exemplo 1: 0.07404685020446777 e
                                                            # exemplo 2: 0.07302403450012207
    print("tempo do Thread: " + str(t2-t1))  # exemplo 1: 0.3122217655181885 e exemplo 2: 0.9106481075286865
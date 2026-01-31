'''
Multiprocessing:
Processes that run in parallel
C.P.U. bound tasks: tasks that are heavy on C.P.U. usage (eg- mathematical computation, data processing)
Parallel Execution: When multiple cores of the C.P.U.
'''
import multiprocessing
import time

def print_square():
    for x in range(5):
        time.sleep(1)
        print(x**2)

def print_2x_letters():
    for x in 'abcde':
        time.sleep(1.5)
        print(x*2)

if __name__=='__main__':
    start_time=time.time()
    # create 2 processes
    p1=multiprocessing.Process(target=print_square)
    p2=multiprocessing.Process(target=print_2x_letters)
    #print_square()
    #print_2x_letters()
    # starting the process
    p1.start()
    p2.start()
    # joining the processes
    p1.join()
    p2.join()
    end_time=time.time()
    print('Time Elapsed:',(end_time-start_time))
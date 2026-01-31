'''
Multiyhreading:
When to use multithreading ?
I/O bound tasks: tasks that spend more time waiting for I/O operations (eg- file operations, network requests)
Concurrent Execution: When you want to improve the throughput of your application by performing multiple operations simulaneously
'''
import threading
import time

def print_numbers():
    for x in range(5):
        time.sleep(2)
        print(f"Number:{x}")

def print_letters():
    for x in 'abcde':
        time.sleep(2)
        print(f"Letter:{x}")

# creating threads
t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letters)


start_time=time.time()
# starting the threads
t1.start()
t2.start()
#print_numbers()
#print_letters()
# joining the 2 threads to the main thread
t1.join()
t2.join()
end_time=time.time()
print("Time Elapsed:",(end_time-start_time))
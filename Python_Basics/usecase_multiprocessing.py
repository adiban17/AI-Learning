'''
Real-World Scenario: C.P.U. Bound Tasks
Scenario: Factorial Calculation
Calcukating the factorial for large numbers requires huge C.P.U. power. Using multiprocessing makes the work easier by distributing the job
across various cores.
'''

# importing required packages
from concurrent.futures import ProcessPoolExecutor
import time
import sys
import math

# increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(10000000)

# defining function to find factorial
def fact(num):
    return(math.factorial(num))

# calling the function
if __name__=="__main__":
    numbers=[1000,7000,2103,2281,1934]
    start_time=time.time()
    with ProcessPoolExecutor(max_workers=3) as executor:
        results=executor.map(fact,numbers)
    end_time=time.time()
    for result in results:
        print(f"Result:{result}")

    print(f"Time Elapsed: {end_time-start_time}")

    # time taken=0.01

'''
nums=[1000,7000,2103,2281,1934]
start_time=time.time()
for num in nums:
    print(fact(num))
end_time=time.time()
print(f"Time Elapsed: {end_time-start_time}")
# time taken=0.02
'''

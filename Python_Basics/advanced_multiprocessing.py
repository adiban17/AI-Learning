'''
Advanced MultiProcessing using ProcessPoolExecutor
'''
from concurrent.futures import ProcessPoolExecutor
import time

def num_square(num):
    time.sleep(1.69)
    return(num**2)

if __name__=="__main__":
    nums=[1,2,3,4,5]

    with ProcessPoolExecutor(max_workers=2) as executor:
        results=executor.map(num_square,nums)

    for result in results:
        print(result)
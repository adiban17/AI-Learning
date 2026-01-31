from logger import logging

def add(a,b):
    logging.debug("Addition is being done")
    return(a+b)

sum=add(10,12)
logging.debug('Function was called')
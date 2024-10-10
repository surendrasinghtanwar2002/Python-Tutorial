## Logging practise

import logging

logging.basicConfig(level=10,filename="log.log",filemode="w",format="%(asctime)s - %(name)s- %(levelname)s - %(message)s")


##logging information message of variable
x = 2
##logging message
logging.info(f"The value of x is {x}")

##First method
try:
    1 / 0

except ZeroDivisionError as e:
    logging.exception("Zero devision error")

##Second Method 
try:
    1/0

except ZeroDivisionError as e:
    logging.error("Zero devision error",exc_info=True)
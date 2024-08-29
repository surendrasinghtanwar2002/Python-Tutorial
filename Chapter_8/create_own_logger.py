import logging

##First step is to customised log level and setup their format
logging.basicConfig(level=10,
                    filename="mydefaultlogger.log",
                    filemode="w",
                    format="%(asctime)s -%(name)s - %(levelname)-s - %(message)s")

##create the logger object
mylogger = logging.getLogger("MyCustomLogger")

## Step for creating custom logger
#(1) first create the custom logger object 
#(2) Second create custom logger file handler
#(3) Third create the custom logger file formater (It is use to store log file in specific pattern)
#(4) after creating the formatter simply add that formater in the handler
#(5) after creating all this simply add handler in the custom logger object

handler = logging.FileHandler('mycustomlogger.log')
formattter = logging.Formatter("%(asctime)s -%(name)s - %(levelname)-s - %(message)s")
handler.setFormatter(formattter)
mylogger.addHandler(handler)



##putting log in seperate log
mylogger.info("This is my custom logger which is made for my script")       ##Custom log created for the script

logging.info("This is the root logger which iss provided by logging module itself")     ##Default log presented in the machine

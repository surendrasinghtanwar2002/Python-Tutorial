import logging

##configuring basic configuration of logs
logging.basicConfig(
    level=10,
    filename="logging.log",
    filemode="w",
    format= "%(asctime)s - %(name)s - %(levelname)s - %(message)s")

##creating custom log object
netmiko_loggers = logging.getLogger("netmiko_logger")        ##This simply creates a logger for you

##create the file handler for the logfile 
handler = logging.FileHandler("my_netmiko_logger.log")

##formatter for the log file
logformatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

##adding format to the file handler 
handler.setFormatter(logformatter)

##add handler to add all this file in main log file
netmiko_loggers.addHandler(handler)

#putting each log in seperate log file 
netmiko_loggers.info("This is the information message of the log file")

logging.info("This is the root log file of the logger")
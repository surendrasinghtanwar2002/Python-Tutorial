import logging

# Step 1: Configuring basic configuration of the root logger
logging.basicConfig(
    level=10,  # Equivalent to logging.DEBUG
    filename="logging.log",
    filemode="w",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# Step 2: Creating a custom logger object
netmiko_loggers = logging.getLogger("netmiko_logger")  # Creates a logger named "netmiko_logger"

# Step 3: Create a file handler for the custom logger
handler = logging.FileHandler("my_netmiko_logger.log")  # This handler will write logs to 'my_netmiko_logger.log'

# Step 4: Create a formatter for the custom logger
logformatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Step 5: Adding the formatter to the handler
handler.setFormatter(logformatter)  # Correct method to set formatter is 'setFormatter'

# Step 6: Add the handler to the custom logger
netmiko_loggers.addHandler(handler)

# Step 7: Logging messages with both the root logger and the custom logger
netmiko_loggers.info("This is the information message of the custom logger file")

logging.info("This is the root logger message")

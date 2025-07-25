import os

print(os.name)
print(os.getlogin())


import logging

logger = logging.getLogger("os")

logger.error("This is an info message from the module_example.py file.")

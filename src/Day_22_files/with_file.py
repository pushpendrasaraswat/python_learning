# This code demonstrates how to read a file using a context manager in Python.
# Using a context manager to open a file
"""
You don’t need to call file.close() because the with statement in Python automatically handles resource management.
The with statement uses something called a context manager. Files in Python are context managers — they implement the __enter__ and __exit__ methods.

__enter__: Opens the file and returns the file object.

__exit__: Automatically closes the file, even if an error occurs inside the block.
"""
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)
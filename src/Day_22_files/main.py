file = open("my_file.txt")

contents = file.read()

print(contents)

# Close the file after reading
# It's a good practice to close files after you're done with them
# to free up system resources.
file.close()
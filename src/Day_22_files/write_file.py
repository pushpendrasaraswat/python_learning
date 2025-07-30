with open("write_file.txt","w") as file:
    # Writing a single line to the file
    file.write("This is a line written to the file.\n")

    # Writing multiple lines to the file
    lines = ["This is the first line.\n", "This is the second line.\n", "This is the third line.\n"]
    file.writelines(lines)


# mode w is to write to a file, if the file already exists it will be overwritten if it does not exist it will be created.
# mode a is to append to a file, if the file does not exist it will be created, if it does exist it will be appended to.
# mode r is to read a file
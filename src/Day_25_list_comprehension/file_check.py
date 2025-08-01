
file1data = []
file2data = []
with open("file1.txt") as file1:
    for line in file1:
        file1data.append(line.strip())  # Using strip() to remove any trailing newline characters


with open("file2.txt") as file2:
    for line in file2:
        file2data.append(line.strip())  # Using strip() to remove any trailing newline characters

result = []
if len(file1data) > len(file2data):
    result = [line for line in file1data if line in file2data]
else:
    result = [line for line in file2data if line in file1data]

print(result)


my_set = {"10", "20", "30", "40", "50", "60", "70", "80", "90", "100", "10","20"}

print(my_set)
print("\n")

# we can do index based in set like in list, but we can convert it to list and then do an index based
# set is not ordered
for element in my_set:
    print(element)

print("\n")
# adding and removing an element from set
my_set.add("110")
my_set.remove("10")

for element in my_set:
    print(element)
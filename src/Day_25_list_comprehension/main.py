
list = [1,2,3]
print(list)
new_list = [n+1 for n in list]
print(new_list)


name = "Angela"

new_list = [letter for letter in name]
print(new_list)

print([i*2 for i in range(1,5)])

# condition list

list_condition= [1,2,3,4,5,6,7,8,9,10]

even_list = [n for n in list_condition if n % 2 == 0]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

short_names = [name for name in names if len(name) < 5]

print(short_names)

upper_names = [name.upper() for name in names if len(name) > 5]

print(upper_names)
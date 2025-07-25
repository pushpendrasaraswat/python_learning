to_minutes = 24*60
to_Seconds = to_minutes*60
name_of_unit="minutes"
name_of_unit_sec="seconds"


data_string = "string data"
dat_int =1
data_float = 1.5
data_bool = True #false
data_list = [1, 2, 3, 4, 5]
data_set = {"a","b","c"}
data_dictionary = {"key1": "value1", "key2": "value2"}


print(f"20 days are {20 * to_minutes}  {name_of_unit}")
print(f"20 days are {20 * to_Seconds}  {name_of_unit_sec}")

print(f"35 days are {35 * to_minutes}  {name_of_unit}")
print(f"35 days are {35 * to_Seconds}  {name_of_unit_sec}")

a = 10
b = 20
total= a + b
print("The sum is", total)
print("The sum is "+str(total)) # Concatenating strings and numbers
print(f"The sum of {a} and {b} is {total}") # Using different ways to format strings and correct way
print("The sum of {} and {} is {}".format(a,b,total)) # old way of formatting strings
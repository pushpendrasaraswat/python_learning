import pandas as pd


data = pd.read_csv("weather_data.csv")
#print(type(data))
#print(data)

#print(type(data["temp"]))

data_dictionary = data.to_dict()
print(data_dictionary)

print("\n\n")
temp_list = data["temp"].to_list()
print(temp_list)
# we can also use the following to get the same result
print(data.temp)

print(f"Average temperature: {sum(temp_list) / len(temp_list)}")
print("mean:", data["temp"].mean())
print ("max:", data["temp"].max())
print("min:", data["temp"].min())

print("\n\n")

print(data["day"])
print("\n\n")

print(data.condition.values)


# HOW TO GET DATA from rows in our dataset

print(data[data.day == "Monday"])


print("Get row where temp is maximum")

max_temp_row = data[data.temp == data.temp.max()]

print("temp row :  ",max_temp_row)

max_temp_data = max_temp_row.temp.item()

farhenheit_temp = (max_temp_data * 9/5) + 32
print(f"temp is  {max_temp_data}  farhenheit temp is {farhenheit_temp}")
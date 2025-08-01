# reading a CSV file
with open("weather_data.csv") as weather_file:
    lines = weather_file.readlines()
    print(lines)

import csv

with open("weather_data.csv") as weather_file:
    weather_data = csv.reader(weather_file)
    temperatures = []
    # to get the data we did lot of things so panda is a good library to use
    for row in weather_data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

    print(temperatures)
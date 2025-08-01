import pandas as pd

data = pd.read_csv("Census_-_Squirrel_Data.csv")

# the task is to find the number of squirrels in each color category
# and print the result in another csv file

#squirrel_counts = data['Primary Fur Color'].value_counts()

grey_squirrels_count = len(data[data['Primary Fur Color'] == 'Gray'])
cinnamon_squirrels_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels_count = len(data[data['Primary Fur Color'] == 'Black'])


print(grey_squirrels_count)
print(cinnamon_squirrels_count)
print(black_squirrels_count)

df = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

dataFram = pd.DataFrame(df)

dataFram.to_csv("Census_-_Squirrel_Counts.csv")
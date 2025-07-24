fruits = ["Cherry", "Apple", "Pear"]

print(fruits[0]) # Cherry
print(fruits[1]) # Apple
fruits[0] = "Grapes" # Changes the first item in the list to Grapes
print(fruits[-1]) # Pear last item in the list
fruits.append("Banana") # Adds an item to the end of the list
fruits.extend(["Cherry","Orange"]) # Adds multiple items to the end of the list

print("-------------List of Fruits-------------")
for fruit in fruits:
    print(fruit)

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

states_of_america[1] = "Pencilvania"

states_of_america.append("Angelaland")

states_of_america.extend(["Angelaland", "Jack Bauer Land"])

print(states_of_america)

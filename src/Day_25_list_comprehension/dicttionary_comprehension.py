
#new_dict = {new_key:ney_value for (key, value) in old_dict.items() if condition}

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
"""
generating a dictionary with names as keys and their lengths as values
student_scores = {
    "Alex": 91,
    "Beth": 89,
    "Caroline": 93,
    "Dave": 85,
    "Eleanor": 88,
    "Freddie": 95
}
"""
import random
new_dict = {item:random.randint(1,100) for item in names}

print(new_dict)

passed_students = {student:score for (student, score) in new_dict.items() if score > 70}

print(passed_students)

# use string comprehension from String
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split()}
print(result)

weather_C = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 13,
    "Saturday": 16,
    "Sunday": 17
}

weather_F = {key:temp * 9/5 + 32 for (key, temp) in weather_C.items()}
print(weather_F)
student_dictionary = {
    "students": ["Angela","Alicia", "Alex"],
    "scores": [56,78,87]
}


for key, value in student_dictionary.items():
    print(key)


# to iterate Data frames in pandas

import pandas as pd

student_data_frame = pd.DataFrame(student_dictionary)

# loop through the data frame
# for (key, value) in student_data_frame.iterrows():
#    print(key)
#    print(value)


for (index, row) in student_data_frame.iterrows():
    #print(index)
    #print(row)
    #print(row.students)
    #print(row.scores)
    if row.students == "Angela":
        print(row.scores)
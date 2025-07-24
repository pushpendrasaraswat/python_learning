student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]



if not student_scores:
    print("No scores available.")
    exit()

print(max(student_scores)) # Find the highest score in a list of student scores

max_score = student_scores[0]

for score in student_scores:
    if score > max_score:
        max_score = score

print(f"The highest score in the class is: {max_score}")


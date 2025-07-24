# calculate BMI
height = 1.65
weight = 84

bmi = weight / (height * height)
# round the BMI to the nearest integer, we can pass number if digit of decimal places we want to round to
print(round(bmi))

#Rounding a Number
print(round(bmi,2))  # round to 2 decimal places

# Original Float with decimal places
print(bmi)

# Flooring the number by converting it into int
print(int(bmi))

# Rounding the number into a whole number
print(round(bmi))

# Rounding only to 2 decimal places
print(round(bmi, 2))


## Accumulate
score = 0

# User scores a point
score += 1
print(score)

#Also
score -= 1
score *= 2
score /= 2

score = 0
height = 1.8
is_winning = True

print(f"Your score is = {score}, your height is {height}. You are winning is {is_winning}")

print(type(int("5")/int(2.7)))
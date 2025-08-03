height = float(input("Height : "))
weight = float(input("Weight : "))

if height > 3:
    raise ValueError("Height must be greater than 3 meters")

bmi = weight/ (height ** 2) # height * height = height **2

print(bmi)
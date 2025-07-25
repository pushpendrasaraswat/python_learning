from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
# bug here was that randint produce a number between 1 and 6, but the list index starts from 0 till 5 so 6 will give error
dice_num = randint(1, 6)

print(dice_num)

print(dice_images[dice_num])

# so correct solution is following

dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_images[dice_num])

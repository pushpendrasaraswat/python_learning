game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

if game_level < 5:
    new_enemy = enemies[1]
# variable inside if, for block is accessible outside of it they dont have block scope
# block space is for methods and functions
else:
    new_enemy = enemies[0]
print(new_enemy)




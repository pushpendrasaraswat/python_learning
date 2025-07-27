class User:
    pass # This class is empty and serves as a placeholder for future attributes and methods.


user1 = User()
# in pyhton we can add attributes to a class instance after it has been created
# dynamic creating attributes are allowed in pyhton
user1.id= 123
user1.name="user"

print(user1)
print(user1.id)
print(user1.name)


user2 = User()

user2.id= 132
user2.name="user2"

print(user2)
print(user2.id)
print(user2.name)
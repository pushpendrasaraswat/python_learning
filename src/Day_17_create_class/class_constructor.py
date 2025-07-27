class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name



user1=User(123, "John Doe")
print(user1)
print(f"{user1.id} is {user1.name}")



user2=User(234, "Jane Smith")
print(user2)
print(f"{user2.id} is {user2.name}")
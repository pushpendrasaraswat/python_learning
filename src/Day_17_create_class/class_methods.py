class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.followers += 1
        print(f"{self.name} followed {user.name}")


user1 = User(user_id=1, user_name="user1")

user2 = User(user_id=2, user_name="user2")

user1.follow(user2)

print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)

from user import User

new_user = User("test_user", "test@test.com","test_password", "Software Engineer")

print(new_user.get_user_info())

new_user.change_password("<PASSWORD>")
new_user.change_job_title("Senior Software Engineer")

print(new_user.get_user_info())

new_user_first = User()
print(new_user_first.get_user_info())

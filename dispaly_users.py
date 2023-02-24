from main import User

my_users = User.select()
for user in my_users:
    print(user.name, user.email, user.password)


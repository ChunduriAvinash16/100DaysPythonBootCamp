class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.follwers = 0
        self.following = 0
    def follow(self,user):
        user.follwers += 1
        self.following += 1


user_1 = User("001", "Avinash")
user_2 = User("002", "Raghu")
user_1.follow(user_2)
user_2.follow(user_1)

print(user_1.follwers)
print(user_1.following)
print(user_2.follwers)
print(user_2.following)
# print(user_1.id)
# print(user_1.username)

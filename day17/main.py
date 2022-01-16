class User:
    def __init__(self,user_id,username):
        self.id = user_id
        self.username = username
        self.follower = 6
        self.following = 7

    def follow(self,user):
        user.follower += 1
        self.following += 1


user_1 = User("001","angela")

# print(user_1.username)
# print(user_1.follower)

user_2 = User("002","jack")

user_1.follow(user_2)

print(user_1.following)
print(user_1.follower)
print(user_2.following)
print(user_2.follower)
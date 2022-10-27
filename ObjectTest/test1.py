class user:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print(self):
        print(self.age, self.name)


if __name__ == '__main__':
    user1 = user("name", 12)
    user.print(user1)
    print(user1.name)
    print(user1.age)
    user1.__setattr__("name1", 13)
    user.print(user1)
    print(user1.name)
    print(user1.age)

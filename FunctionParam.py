import numpy
class Animal:
    name = "zhangsan"
    age = 12
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age


if __name__ == '__main__':
    dog = Animal("LISI", 12)
    print(dog.get_name())
    print(dog.get_age())




class Person:
    def __init__(self, name_param):
        self.name = name_param
        print("created name : ", self, self.name)

    def talk(self):
        print("name is ", self.name)


person_1 = Person("이름 1")
person_2 = Person("이름 2")

print(person_1.name)
print(person_2.name)

person_1.talk()
person_2.talk()


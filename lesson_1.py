class Person:

    # магический метод
    def __init__(self,name,age):
        self.name=name
        self.age=age

    # метод -функция деф


    def __str__(self):
        # return 'привет'
        return f'{self.name} {self.age} '

    def __len__(self):
        return len(self.name)




#обьект\экземпляр
beka=Person('beka',21)
beka2=Person('бека',99)
print(beka)
print(len(beka))
beka.nameprint()
beka2.nameprint()
# Person.nameprint(beka)
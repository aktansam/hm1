class SuperHero:
    people = 'people'
    # магический метод
    def __init__(self,name,nickname,age,superpower,health_points,catchphrase,damage):
        self.name=name
        self.nickname=nickname
        self.age=age
        self.superpower=superpower
        self.health_points=health_points
        self.catchphrase=catchphrase
        self.damage = damage
        self.fly = False  # По умолчанию fly равен False

    # метод -функция деф

    def nameprint(self):
        print("My Name is ",self.name)

    def double_health(self):
        self.health_points **= 2
        self.fly = True
    def __str__(self):
        return f"nickname: {self.nickname}, superpower: {self.superpower}, health points: {self.health_points}"

    def __len__(self):
        return len(self.catchphrase)

class AirHero(SuperHero):
    def __init__(self, name, nickname,age,superpower, health_points, catchphrase, damage, altitude):
        super().__init__(name, nickname, age,superpower, health_points, catchphrase, damage)
        self.altitude = altitude
        self.fly = False

    def double_health(self):
        self.health_points **= 2
        self.fly = True

    def true_phrase(self):
        print(f"True in the True_phrase: {self.fly}")

class GroundHero(SuperHero):
    def __init__(self, name,nickname,age,superpower, health_points, catchphrase, damage, speed):
        super().__init__(name, nickname,age,superpower, health_points, catchphrase, damage)
        self.speed = speed
        self.fly = False

    def double_health(self):
        self.health_points **= 2
        self.fly = True

    def true_phrase(self):
        print(f"True in the True_phrase: {self.fly}")

class Villain(GroundHero):
            people = 'monster'

            def __init__(self,name, nickname, age,superpower, health_points, catchphrase, damage, speed):
                super().__init__(name, nickname,age, superpower, health_points, catchphrase, damage, speed)

            def gen_x(self):
                pass

            def crit(self):
                self.damage **= 2

#обьект\экземпляр
Hulk=SuperHero('Hulk',"Doc",21,"Gamma Radiation",100,"Hulk smash!", 500)
air_hero = AirHero("Clark Kent", "Superman", 40,"Flight",100, "Up, up, and away!", 50, 1000)
ground_hero = GroundHero("Bruce Wayne","Batman",33,"Stealth",100, "I am the night!",30,80)

villain=Villain("Joker","Clown Prince of Crime",37,"Chaos",120,"Why so serious?",40,70)

Hulk.nameprint()# Выводит имя героя
print(Hulk)  # Выводит прозвище героя, его суперспособность и его здоровье
print(len(Hulk))  # Считает длину коронной фразы героя
Hulk.double_health()  # Умножает здоровье героя на 2
print(Hulk)

air_hero.nameprint()
print(air_hero)
air_hero.double_health()
print(air_hero)
air_hero.true_phrase()

ground_hero.nameprint()
print(ground_hero)
ground_hero.double_health()
print(ground_hero)
ground_hero.true_phrase()


print(villain)
villain.crit()
print(f"Damage after crit: {villain.damage}")
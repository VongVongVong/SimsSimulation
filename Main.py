import random


class Human:
    def __init__(self, name="Human", job=None, car=None, home=None):
        self.name = name
        self.money = 100
        self.happiness = 50
        self.car = car
        self.hunger = 100
        self.job = job
        self.home = home

    def get_home(self):
        self.home = House()

    def get_job(self):
        self.job = Job(job_list)

    def get_car(self):
        self.car = Car(brands_of_car)

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.hunger > 95:
                self.hunger -= 100 - self.hunger
                self.hunger = 100
                return
            self.hunger += 5
            self.home.food -= 5

    def drive_car(self):
        if self.car.drive():
            return True
        else:
            if self.car.fuel < self.car.consumption:
                self.shopping("fuel")
            else:
                self.car.repair()
                return False

    def shopping(self, items):
        if items == "fuel":
            print("I bought fuel")
            self.money -= 100
            self.car.pump_gas()
        if self.car.drive():
            return
        else:
            if self.car.fuel < self.car.consumption:
                items = "fuel"
            else:
                self.car.repair()
                return

        if items == "food":
            print("Bought food")
            self.money -= 50
            self.home.food += 50
        elif items == "fuel":
            print("I bought fuel")
            self.money -= 100
            self.car.pump_gas()


    def work(self):
        if self.car.drive():
            return
        self.money += self.job.salary
        self.happiness -= self.job.gladness_less
        self.hunger -= 4

    def chill(self):
        pass

    def days_indexes(self, day):
        pass

    def is_alive(self):
        pass

    def live(self, day):
        pass



class Car:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.max_fuel = brand_list[self.brand]["fuel"]
        self.fuel = self.max_fuel
        self.max_durability = brand_list[self.brand]["durability"]
        self.durability = self.max_durability
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.fuel >= self.consumption and self.durability > 0:
            self.fuel -= 1
            self.durability -= 1
            return True
        else:
            print("The car is out of fuel")
            return False

    def repair(self):
        self.durability = self.max_durability
        #rapair only 20+ durability

    def pump_gas(self):
        self.fuel = self.max_fuel
        #calculate the cost depending on galons



class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]


job_list = {
    "python developer": {"salary": 40, "gladness_less": 5},
    "java developer": {"salary": 55, "gladness_less": 15},
    "C# developer": {"salary": 50, "gladness_less": 10},
    "C++ developer": {"salary": 60, "gladness_less": 25},
    "Swift developer": {"salary": 55, "gladness_less": 20},
}


class House:
    def __init__(self):
        self.food = 0
        self.mess = 0
        #add space



brands_of_car = {
    "Toyota":{"fuel": 18, "durability": 150, "consumption": 3},
    "BMW":{"fuel": 20, "durability": 80, "consumption": 5},
    "Honda": {"fuel": 14, "durability": 130, "consumption": 3},
    "Mercedes": {"fuel": 21, "durability": 95, "consumption": 6},
    "Audi": {"fuel": 19, "durability": 90, "consumption": 5},
    "Ford": {"fuel": 17, "durability": 120, "consumption": 4}
}


nick = Human("Nick")
jeb = Human("Jeb")

car1 = Car(brands_of_car)
car2 = Car(brands_of_car)

print(car1.brand)
print(car2.brand)
import random


class Human:
    def __init__(self, name="Human", job=None, car=None, home=None):
        self.name = name
        self.money = 100
        self.Happiness = 50
        self.car = car
        self.job = job
        self.home = home

    def get_home(self):
        pass

    def get_job(self):
        pass

    def get_car(self):
        pass

    def eat(self):
        pass

    def work(self):
        pass

    def chill(self):
        pass

    def days_indexes(self, day):
        pass

    def is_alive(self):
        pass

    def live(self, day):
        pass




class Car:
    def __init__(self, brand, fuel, consumption, durability, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.durability = brand_list[self.brand]["durability"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.fuel >= self.consumption and self.durability > 0:
            self.fuel -= 1
            self.durability -= 1
            return True
        else:
            print("The car is out of fuel")
            return False



class Job:
    def __init__(self):
        pass


class Home:
    def __init__(self):
        pass



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

car = Car("Toyota")

car.add_passanger(nick)
car.add_passanger(jeb)
car.print_passangers()
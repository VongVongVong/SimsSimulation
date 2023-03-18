# class Parent:
#     classmetods and attrs
# class Child(Parent):
#     classmethods and attrs

class Class1:
    var = 20
    def __init__(self):
        self.var = 10

class Class2(Class1):
    def __init__(self):
        print(self.var)
        super().__init__()
        print(self.var)
        print(super().var)

ccc = Class2()

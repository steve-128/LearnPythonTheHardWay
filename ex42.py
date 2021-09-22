## Animal is- a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is a object
class Dog(Animal):
    def __init__(self, name):
        ## dog  has a name
        self.name = name

## cat is a object
class Cat(Animal):
    def __init__(self, name):
        ## a cat  has a name
        self.name = name

## person is a object and has a pet
class Person(object):
    def __init__(self, name):
        ## a person has a name
        self.name = name
        ## Person has- a pet of some kind
        self.pet = None

## ??
class Employee(Person):
    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## set the employee salary
        self.salary = salary

## a fist is a object
class Fish(object):
    pass

## a salmon is a object
class Salmon(Fish):
    pass

## a salmon is a object
class Halibut(Fish):
    pass


## rover is- a Dog
rover = Dog("Rover")

## satan is a cat
satan = Cat("Satan")

## Mary is a person
mary = Person("Mary")

## mary's pet is satan
mary.pet = satan

## frank is an employee with the salary of 120000
frank = Employee("Frank", 120000)

## frank's pet is rover
frank.pet = rover

## flipper is a fish
flipper = Fish()

## crouse is a salmon
crouse = Salmon()

## harry is a Halibut
harry = Halibut()

'''
study drills
2. yes 
6. yes it's possible
'''
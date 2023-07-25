# Write a Python class for an Animal that has a name and energy attributes. The animal class should also have methods for eat, sleep, and play that will take in an integer and increase/decrease the energy of the animal with a formatted print statement

class Animal():

    def __init__(self, name, energy):
        self.name = name
        self.energy = energy
    
    def eat(self, num):
        self.energy += num
        if num > 20:
            print(f'{self.name} ate too much. Time to play!')
        else:
            print(f"{self.name}'s energy went up to {self.energy} after eating {num} treats")

    def sleep(self, num):
        self.energy += num
        print(f"{self.name}'s energy went up to {self.energy} after sleeping for {num} minutes")

    def play(self, num):
        self.energy -= num
        if self.energy <= 0:
            print(f"{self.name} played too much. Time to go to sleep!")
        else:
            print(f"{self.name}'s energy went down to {self.energy} after playing for {num} minutes")

animal1 = Animal('Peter', 10)
animal2 = Animal('Rupert', 20)

animal1.eat(10)
animal2.sleep(30)
animal1.play(5)
animal2.play(15)
animal1.play(50)
animal2.eat(30)
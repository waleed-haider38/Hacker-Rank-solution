class Animal:
    name = ""

    def speaks(self):
        print("It can make sounds")
    
class Dog(Animal):
    name = ""

    def speaks(self):
        super().speaks()
        print("Dog can bark")
    
class Cat(Animal):
    name =""

    def speaks(self):
        super().speaks()
        print("Cats Meow")

cat = Cat()
dog = Dog()

cat.speaks()
dog.speaks()
class Studnet:
    name = ""
    age = 1

    def __init__(self, name , age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"The Name of student is {self.name}. He is {self.age} years old")
    
    def is_adult(self):
        if self.age >= 18:
            print("Adult")
        else:
            print("Not an Adult")

class Teacher:
    name = ""
    salary = 1000
    age = 1

    def __init__(self , name , salary, age):
        self.name = name
        self.salary = salary
        self.age = age

    def into(self):
        print(f"The Name of Teacher is {self.name} , his age is {self.age} and his salary is {self.salary}")

    def retire(self , others):
        if self.age > 50:
            print("The teacher has been retired")
        else:
            print("This teacher is active now")
            


t1 = Teacher("Azam sahib" , 50000 , 45)
t1.into()
t1.retire(45)



# std1 = Studnet("Waleed Haider" , 23)


# std2 = Studnet("Muhammad Bin Qasim" , 17)


# std1.display_info()
# std1.is_adult()

# std2.display_info()
# std2.is_adult()
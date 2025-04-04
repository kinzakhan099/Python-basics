#class with constructor
class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def display_info(self):
        print(f"Name: {self.name} \nAge: {self.age}\nGrade: {self.grade}")

print("Class with constructor")
s1=Student("Kinza",20,"A")
s1.display_info()
s2=Student("Hajira",22,"A+")
s2.display_info()
s3=Student("Ali",23,"B")
s3.display_info()
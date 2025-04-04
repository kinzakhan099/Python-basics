#class without constructor

class Student:
    name="Unknown"
    age=0
    grade="default"

    def display_info(self):
        print(f"Name: {self.name} \nAge: {self.age}\nGrade: {self.grade}")
print("Class without constructor")
s1=Student()
s1.name="Kinza"
s1.age=20  
s1.grade="A"
s1.display_info()
s2=Student()
s2.name="Hajira"
s2.age=22
s2.grade="A+"
s2.display_info()
s3=Student()
s3.display_info()
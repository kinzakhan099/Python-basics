#Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #print person details
    def display_person(self):
        return f"Name: {self.name}, \nAge: {self.age}"
    
    #tells if the person is an adult or not
    def is_adult(self):
        if self.age>=18:
            return True
        else:
            return False

#child class inheriting from Person
class Student(Person):

    #constructor for student class
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id=student_id
        self.courses=[]

    #print student details
    def display_student(self):
        print(f"{super().display_person()}, \nStudent ID: {self.student_id}")

    #enroll in a course
    def enroll(self,course_name):
        self.courses.append(course_name)
        print(f"{self.name} has enrolled in {course_name}")

    #display list of courses a student is enrolled in.
    def list_courses(self):
        if self.courses:
            print(f"{self.name} is enrolled in the following courses:")
            for course in self.courses:
                print(f" - {course}")
        else:
            print(f"{self.name} is not enrolled in any courses")

S1=Student("Ali", 20, "S1245")
S1.display_student()
S1.enroll("Python Programming")
S1.enroll("Data Structures")
S1.enroll("Marketing")
if S1.is_adult():
    print(f"{S1.name} is an adult.")
else:
    print(f"{S1.name} is a minor.")

S1.list_courses()

S2=Student("Sara", 17, "S5321")
S2.display_student()
S2.enroll("Python Programming")
S2.enroll("Data Structures")
S2.enroll("Marketing")
S2.list_courses()
S2.is_adult()
if S2.is_adult():
    print(f"{S2.name} is an adult.")
else:
    print(f"{S2.name} is a minor.")


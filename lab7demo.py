# ----------------- SYSTEM UTILITIES ------------------
class LoginSystem:
    def __init__(self):
        self.credentials = {}  # username: password

    def register(self, username, password):
        self.credentials[username] = password
        print(f"[REGISTERED] {username} successfully.")

    def login(self, username, password):
        return self.credentials.get(username) == password


class AcademicRecordSystem:
    def __init__(self):
        self.records = {}

    def add_record(self, student_id, course, grade):
        self.records.setdefault(student_id, []).append((course, grade))
        print(f"[RECORD ADDED] {course}: {grade} for student {student_id}.")

    def get_records(self, student_id):
        return self.records.get(student_id, [])


# ----------------- BASE CLASS ------------------
class Person:
    def __init__(self, name, person_id):
        self.__name = name
        self.__id = person_id

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id


# ----------------- ROLES ------------------
class Student(Person):
    def __init__(self, name, student_id, login_system, record_system):
        Person.__init__(self, name, student_id)
        self.username = f"stu_{student_id}"
        self.login_system = login_system
        self.record_system = record_system

    def register(self, password):
        self.login_system.register(self.username, password)

    def login(self, password):
        return self.login_system.login(self.username, password)

    def view_records(self):
        records = self.record_system.get_records(self.get_id())
        if records:
            print(f"\n[RECORDS] {self.get_name()} ({self.get_id()}):")
            for course, grade in records:
                print(f"  {course}: {grade}")
        else:
            print("[RECORDS] No academic records found.")

    def student_menu(self):
        while True:
            print("\nStudent Menu:")
            print("1. View Records")
            print("2. Add Course Grade")
            print("3. Exit")
            choice = input("Choose an option: ").strip()
            if choice == "1":
                self.view_records()
            elif choice == "2":
                course = input("Enter course name: ")
                grade = input("Enter grade: ")
                self.record_system.add_record(self.get_id(), course, grade)
            elif choice == "3":
                print("[EXIT] Goodbye, student!")
                break
            else:
                print("Invalid option. Try again.")


class Teacher(Person):
    def __init__(self, name, teacher_id, login_system, record_system):
        Person.__init__(self, name, teacher_id)
        self.username = f"teach_{teacher_id}"
        self.login_system = login_system
        self.record_system = record_system

    def register(self, password):
        self.login_system.register(self.username, password)

    def login(self, password):
        return self.login_system.login(self.username, password)

    def manage_profile(self):
        print(f"[PROFILE] Managing profile for {self.get_name()}.")

    def add_grade_for_student(self):
        student_id = input("Enter student ID: ")
        course = input("Enter course name: ")
        grade = input("Enter grade: ")
        self.record_system.add_record(student_id, course, grade)

    def view_student_records(self):
        student_id = input("Enter student ID to view records: ")
        records = self.record_system.get_records(student_id)
        if records:
            print(f"\n[RECORDS] for Student ID {student_id}:")
            for course, grade in records:
                print(f"  {course}: {grade}")
        else:
            print("No records found for this student.")

    def teacher_menu(self):
        while True:
            print("\nTeacher Menu:")
            print("1. Manage Profile")
            print("2. View Student Records")
            print("3. Add Grade for Student")
            print("4. Exit")
            choice = input("Choose an option: ").strip()
            if choice == "1":
                self.manage_profile()
            elif choice == "2":
                self.view_student_records()
            elif choice == "3":
                self.add_grade_for_student()
            elif choice == "4":
                print("[EXIT] Goodbye, teacher!")
                break
            else:
                print("Invalid option. Try again.")


class TeachingAssistant(Person):
    def __init__(self, name, ta_id, login_system, record_system):
        Person.__init__(self, name, ta_id)
        self.username = f"ta_{ta_id}"
        self.login_system = login_system
        self.record_system = record_system

    def register(self, password):
        self.login_system.register(self.username, password)

    def login(self, password):
        return self.login_system.login(self.username, password)

    def assist_class(self):
        print(f"[ASSIST] {self.get_name()} is assisting a class.")

    def view_records(self):
        records = self.record_system.get_records(self.get_id())
        if records:
            print(f"\n[RECORDS] {self.get_name()} ({self.get_id()}):")
            for course, grade in records:
                print(f"  {course}: {grade}")
        else:
            print("[RECORDS] No academic records found.")

    def ta_menu(self):
        while True:
            print("\nTeaching Assistant Menu:")
            print("1. View My Records")
            print("2. Add My Course Grade")
            print("3. Assist Class")
            print("4. Exit")
            choice = input("Choose an option: ").strip()
            if choice == "1":
                self.view_records()
            elif choice == "2":
                course = input("Enter course name: ")
                grade = input("Enter grade: ")
                self.record_system.add_record(self.get_id(), course, grade)
            elif choice == "3":
                self.assist_class()
            elif choice == "4":
                print("[EXIT] Goodbye, TA!")
                break
            else:
                print("Invalid option. Try again.")


# ----------------- SYSTEM DRIVER ------------------
def main():
    login_sys = LoginSystem()
    record_sys = AcademicRecordSystem()

    while True:
        print("\nWelcome to the University Digital Ecosystem!")
        role = input("Enter your role (student / teacher / ta): ").strip().lower()
        if role not in ("student", "teacher", "ta"):
            print("Invalid role. Please try again.")
            continue

        name = input("Enter your name: ")
        person_id = input("Enter your ID: ")

        while True:
            password = input("Create your password: ")
            confirm = input("Re-enter your password: ")
            if password == confirm:
                break
            else:
                print("Passwords do not match.")
                retry = input("Do you want to try again or change role? (retry/change): ").strip().lower()
                if retry == "change":
                    break
        else:
            continue  # Passwords matched

        # Role initialization
        if role == "student":
            user = Student(name, person_id, login_sys, record_sys)
        elif role == "teacher":
            user = Teacher(name, person_id, login_sys, record_sys)
        elif role == "ta":
            user = TeachingAssistant(name, person_id, login_sys, record_sys)

        user.register(password)

        # Login
        print("\nLogin to continue.")
        while True:
            attempt = input("Enter your password: ")
            if user.login(attempt):
                break
            else:
                print("Incorrect password.")
                try_again = input("Try again? (yes/no): ").strip().lower()
                if try_again != "yes":
                    print("Exiting system.")
                    return

        # Role-specific menu
        if role == "student":
            user.student_menu()
        elif role == "teacher":
            user.teacher_menu()
        elif role == "ta":
            user.ta_menu()

        break  # Done with system


if __name__ == "__main__":
    main()

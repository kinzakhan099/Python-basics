class StudentProfileSystem:
    #constructor to initialize the attributes
    def __init__(self): 
        self.full_name=""
        self.age=0
        self.email=""
        self.course=""

    # 1. User Profile Input
    #asking the user to input their profile details   
    def get_user_profile(self):
        self.full_name=input("Enter your full name: ")
        self.age=int(input("Enter your age: "))
        self.email=input("Enter your email address: ")
        self.course=input("Enter your enrolled course: ")

    #Displaying the user profile
    def display_user_profile(self):
        print("\nUser Profile")
        print(f"Assalam o alikum,{self.full_name}!")
        print(f"Your age:{self.age}")
        print(f"Your email Address:{self.email}")
        print(f"Your enrolled Courses:{self.course}")

    #2. Age Verification
    #checking if the user is eligible to enroll (must be 18+)

    def age_verification(self):
        if self.age<18:
            print("Sorry, you must be 18 or older to proceed.")
            return False
        else:
            print("Access granted.")
            return True
    
    #3. Progress Calculator
    #Calculating and displaying the percentage of course completed

    def calculate_progress(self):
        course_duration=int(input("\nEnter the total duration of the course in weeks: "))
        total_weeks_completed=int(input("Enter the total weeks you have completed: "))
        progress_percentage=(total_weeks_completed/course_duration)*100
        print(f"Your progress is:{progress_percentage:.2f}%")

    #4. Feedback Loop
    #asking the student to rate the course and displaying stars based on the rating

    def get_feedback(self):
        while True:
            try:
                rating=int(input("\nRate the course from 1 to 5: "))
                if 1<=rating<=5:
                    break
                else:
                    print("Please enter a valid rating between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 5.")

        print("Your Rating: ",end="")
        for _ in range(rating):
            print("★",end="")
        print(f"({rating}/5)")

    #5. String Processing
    #Processing the student's review using string methods

    def process_review(self):
        review=input("\nEnter a short review on the course: ")
        review_lowercase=review.lower()
        good_count=review_lowercase.count("good")
        review_updated=review_lowercase.replace("boring","challenging")

        print("\nString Processing Results:")
        print(f"Your review in lowercase letter:\n{review_lowercase}")
        print(f"The word 'good' appears {good_count} time(s) in your review.")
        print(f"Your review after replacing 'boring' with 'challenging':\n{review_updated}")

#main function to run the system
def main():
    system=StudentProfileSystem()
    while True:
        #1: User Profile Input
        system.get_user_profile()

        #2: Display User Profile
        system.display_user_profile()

        #3: Age Verification
        if not system.age_verification():
            retry=input("Do you want to try again? (yes/no): ").strip().lower()
            if retry!="yes" and retry!="y":
                print("Exiting the system. Goodbye!")
                break
            else:
                continue
 
        #4: Progress Calculator
        system.calculate_progress()

        #5: Feedback Loop
        system.get_feedback()

        #6: String Processing
        system.process_review()

        # Exit after successful completion
        print("\nThank you for using the Student Profile System!")
        break


#Run the system
if __name__=="__main__":
    main()
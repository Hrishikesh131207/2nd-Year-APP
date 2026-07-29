class Course:
    def __init__(self, name, duration, fee):
        self.name = name
        self.duration = duration
        self.fee = fee

    def category(self):
        if self.duration <= 6:
            return "Short-Term"
        return "Long-Term"

    def display(self):
        print("\nCourse Name :", self.name)
        print("Duration :", self.duration, "months")
        print("Fee :", self.fee)
        print("Category :", self.category())


class Institute:
    def __init__(self):
        self.courses = []

    def add_course(self):
        name = input("Enter Course Name: ")
        duration = int(input("Enter Duration (months): "))
        fee = float(input("Enter Fee: "))
        self.courses.append(Course(name, duration, fee))
        print("Course Added Successfully!")

    def display_courses(self):
        if len(self.courses) == 0:
            print("No courses available.")
        else:
            i = 0
            while i < len(self.courses):
                self.courses[i].display()
                i += 1


institute = Institute()

while True:
    print("\n1. Add Course")
    print("2. Display All Courses")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        institute.add_course()
    elif choice == 2:
        institute.display_courses()
    elif choice == 3:
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")
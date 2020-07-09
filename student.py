from person import Person

class Student(Person):
    def __init__(self, name, age, studentID):
        # calls the base class constructor
        super().__init__(name, age)
        studentID = studentID

    def studies(self):
    print(f"{self.Name} is studying")
    print(f"{}")
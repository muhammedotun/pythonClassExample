from Person import Person

class Student(Person):
    """docstring for student."""

    def __init__(self, number, name, lastname, course):
        super().__init__(number, name , lastname)
        self.course = course
        course.courseCapasity -= 1

    def printStudent(self):
        print("number: " , self.personNumber , " name: "+ self.personName , self.personLastName ,"course:", self.course.courseName +"\n")

from Student import Student
from Teacher import Teacher
from course import course

class main:
    # crate teacher and course

    muhammedotun = Teacher(1,"muhammed", "Ötün")
    python101 = course("python101", muhammedotun, 3)

    # crate teacher and course

    # crate list
    studentList = []
    # create list


    def addStudent(studentList, stdNumber, stdName, stdLastName, course):
        print(course.courseCapasity)
        if course.courseCapasity > 0:
            studentList.append(Student(stdNumber,stdName,stdLastName,course))
        else:
            print("the course is full")

    def printStudentList(studentList):
        for student in studentList:
            student.printStudent()

    addStudent(studentList, 1, "emirhan", "eren", python101)
    addStudent(studentList, 2, "yahya furkan", "kılıçoğlu", python101)
    addStudent(studentList, 3, "onur", "kerim", python101)
    addStudent(studentList, 4, "kasım", "eren", python101)

    printStudentList(studentList)
if __name__ == '__main__':
    main()

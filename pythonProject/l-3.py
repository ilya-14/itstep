'''class Student:
    print("Hi")
    def __init__(self):
        self.height = 160
        print(self)

first_student = Student()'''

'''class Student:
    def __init__(self):
        self.height = 160
        print(self)

first_student = Student()
Student.__init__(self=first_student)
print(first_student.height)'''

'''class Student:
    def __init__(self, height=165):
        self.height = height

first_student = Student()
viktor = Student(height=180)
print(first_student.height)
print(viktor.height)'''

'''class Student:
    amount_of_students = 0
    def __init__(self, height=160):
        self.height = height
        Student.amount_of_students+=1

nick = Student ()
kate = Student(height=170)
print(nick.amount_of_students)
print(Student.amount_of_students)'''

class Student:
 amount_of_students = 0
 def __init__(self, height=160):
     self.height = height
     Student.amount_of_students+=1
 def grow(self, height=1):
     self.height+=height
nick = Student()
print(nick.height)
kate = Student(height=170)
print(kate.height)
nick.grow(height=15)
print(nick.height)
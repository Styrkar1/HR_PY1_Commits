class Person():
    def __init__(self,name,user,SSN):
        self.name = name
        self.user = user
        self.SSN = SSN

    def GetName(self):
        return self.name

    def GetUserName(self):
        return self.user

    def GetSSN(self):
        return self.SSN

class Course():
    def __init__(self,name,students,professor):
        self.name = name
        self.students = students
        self. professor = professor

    def GetName(self):
        return self.name

    def GetStudents(self):
        return self.students

    def GeProfessor(self):
        return self.professor

class Student(Person,Course):
    def __init__(self,name,user,SSN,Department):
        Person.__init__(self,name = "",user = "",SSN = 0)
        Course.__init__(self,name = "",students = [],professor = "")
        self.Department = Department

    def GetDepartment(self):
        return self.Department

class Professor(Person,Course):
    def __init__(self,position):
        Person.__init__(self,name = "",user = "",SSN = 0)
        Course.__init__(self,name = "",students = [], professor = "")
        self.position = position

    def GetPosition(self):
        return self.position


        
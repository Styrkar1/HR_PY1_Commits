class Student():
    def __init__(self,student_id,grades):
        self.student_id = student_id
        self.grades = [float(x) for x in grades]

    def get_average(self):
        total = 0
        for i in self.grades:
            total += i
        average = total / len(self.grades)
        return average

    def __str__(self):
        return "Student ID: {}\nGrades: {}".format(self.student_id,self.grades)

    def __lt__(self,other):
        average = self.get_average()
        other_avg = other.get_average()
        if average < other_avg:
            return True
        return False



def main():
    student_id = input("Enter student ID: ")
    grades = input("Enter 4 grades seperated by a comma").split(",")
    john = Student(student_id, grades)

    student_id = input("Enter student ID: ")
    grades = input("Enter 4 grades seperated by a comma").split(",")
    alice = Student(student_id, grades)

    print("John's info")
    print(john)

    if (john < alice):
        print("John has a lower average grade than Alice")
    else:
        print("Alice has a lower average grade than John")

main()
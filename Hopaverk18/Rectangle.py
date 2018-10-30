class Rectangle():
    def __init__(self,width=0,length=0):
        self.__width = width
        self.__length = length

        if width < 0:
            width = 0

        if length < 0:
            length = 0

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return self.__length * 4

    def __repr__(self):
        return ""

    def __eq__(self,other):
        if self.area == other.area:
            return True
        else:
            return False

    def __str__(self):
        return "Length: {}, Width: {}".format(self.__length, self.__width)


obj1 = Rectangle(10, 2)
obj2 = Rectangle(2, 10)
print(obj1.area()) == print('20')
print(obj1.perimeter()) == print('24')
print(obj2.area()) == print('20')
print(obj2.perimeter()) == print('24')
print(obj1.__repr__()) == print('Rectangle(10,2)')
print(obj1 == obj2) == print('True')

assert obj1.area() == 20
assert obj1.perimeter() == 24
assert obj2.area() == 20
assert obj2.perimeter() == 24
assert obj1.__repr__() == 'Rectangle(10,2)'
assert str(obj1 == obj2) == 'True'
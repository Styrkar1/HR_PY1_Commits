def main():
   # Create some vehicles
   v1 = Vehicle("AB 123", 2010)
   c1 = Car("SF 735", 2007, "Station")
   t1 = Truck("TU 765", 1994, 6)
   b1 = Motorbike("XY 666", 2005)
   c1.set_weight(3500)
   t1.set_weight(9000)
   b1.set_CC(250)
   # Print info
   print(v1)
   print(c1)
   print("The weight of the car is: {:.2f}".format(c1.get_weight() ))
   print(t1)
   print("The fee for the truck is: {:.2f}".format(t1.get_fee() ))
   print(b1)
   print("The CC of the bike is: {:.2f}".format(b1.get_CC() ))
   print()
   thelist = [v1,c1,t1,b1]
   for i in thelist:
       print(i)
   v1 = c1
   print(v1)
   print()
#what's up, the code works by the way but i'm not sure how the submission works and there's probably some spelling errors, so enjoy

class Vehicle():
    def __init__(self,license_num = "",year = 0):
        self.license_num = license_num
        self.year = year

        self.weight = 0.0
        self.fee = 0.0
    
    def getlicence(self):
        return self.license_num
    
    def getyear(self):
        return self.year

    def setfee(self,inp):
        self.fee = inp

    def set_weight(self,inp):
        self.weight = inp

    def __str__(self):
        return "Vehicle: " + str(self.license_num) + " " + str(self.year) + " Weight=" + str(self.weight) + " Fee=$" + str(self.fee)
   
class Car(Vehicle):
    def __init__(self,license_num,year,style = ""):
        Vehicle.__init__(self,license_num="",year=0)
        self.license_num = license_num
        self.style = style
        self.year = year

    def set_weight(self,num):
        self.weight = num
        if self.weight < 3000:
            self.fee = 30
        elif 3000 <= self.weight < 5000:
            self.fee = 40
        else:
            self.fee = 50

    def get_weight(self):
        return self.weight

    def __str__(self):
        return "Car: " + str(self.license_num) + " " + str(self.year) + " " + str(self.style) + " weight=" + str(self.weight) + " Fee=$" + str(self.fee)

class Truck(Vehicle):
    def __init__(self,license_num,year,wheels = 0):
        Vehicle.__init__(self,license_num="",year=0)
        self.license_num = license_num
        self.wheels = wheels
        self.year = year

    def set_weight(self,num):
        self.weight = num
        if self.weight < 3000:
            self.fee = 40
        elif 3000 <= self.weight < 5000:
            self.fee = 50
        elif 5000 <= self.weight < 10000:
            self.fee = 60
        else:
            self.fee = 50

    def get_fee(self):
        return self.fee
    
    def __str__(self):
        return "Truck: " + str(self.license_num) + " " + str(self.year) + " " + str(self.wheels) + " wheels weight=" + str(self.weight) + " Fee=$" + str(self.fee)

class Motorbike(Vehicle):
    def __init__(self,license_num,year,cc = 0):
        Vehicle.__init__(self,license_num="",year=0)
        self.license_num = license_num
        self.cc = cc
        self.year = year

    def set_CC(self,num):
        self.cc = num
        if self.cc < 50:
            self.fee = 10
        elif 50 <= self.weight < 200:
            self.fee = 20
        else:
            self.fee = 35

    def get_CC(self):
        return self.cc

    def __str__(self):
        return "Motorbike: " + str(self.license_num) + " " + str(self.year) + " " + str(self.cc) + " cc Fee=$" + str(self.fee) 


main()
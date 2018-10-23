class Clock():
    def __init__(self,hours = 00,minutes = 00,seconds = 00):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    def str_update(self,time):
        Nhours,Nminutes,Nseconds = time.split(":")

        self.hours = int(Nhours)
        self.minutes = int(Nminutes)
        self.seconds = int(Nseconds)

    def add_clocks(self,Oclock):
        THours = int(Oclock.hours) + int(self.hours)
        TMinutes = int(Oclock.minutes) + int(self.minutes)
        Tseconds = int(Oclock.seconds) + int(self.seconds)

        if Tseconds >= 60:
            TMinutes += 1
            Tseconds -= 60   

        if TMinutes >= 60:
            THours += 1
            TMinutes -= 60     

        if THours >= 24:
            THours -= 24

        clock = Clock(THours,TMinutes,Tseconds)
        return clock

    def __str__(self):
        return ("{} hours, {} minutes and {} seconds").format(self.hours,self.minutes,self.seconds)

clock1 = Clock()
clock2 = Clock()
print(clock1)
print(clock2)
assert str(clock1) == "0 hours, 0 minutes and 0 seconds"

clock1.str_update("03:21:34")
clock2.str_update("05:45:52")
print(clock1)
print(clock2)
assert str(clock2) == "5 hours, 45 minutes and 52 seconds"

clock3 = clock1.add_clocks(clock2)
print(clock3)
assert str(clock3) == "9 hours, 7 minutes and 26 seconds"
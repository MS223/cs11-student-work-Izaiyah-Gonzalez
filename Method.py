class Time(object):
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    def __str__(self):
        return str(self.hour) + ":" + str(self.minute) + ":" + str(self.second)
    def __add__(self, other):



time1 = Time(5,32,0)
time2 = Time(8,4,36)
time3 = Time(0,22,58)

print time1

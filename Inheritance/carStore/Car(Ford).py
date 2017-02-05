import Car

class Ford(Car):
    def __init__(self):
        print "Balls."

    def breakLvl(self):
        print "car's break lvl is %s"% Car.breakLvl


f = Ford()
f.breakLvl()
f.setTotKm(200)

class Car:
    color = ""
    totKm = 0
    skruer = []
    price = 0
    breakLvl = 0

    def __init__(self):
        print "Damn, for en bil!"

    def getColor(self ):
        print "This!%s" % Car.color

    def getTotKm(self):
        print "%s" % Car.totKm

    def setTotKm(self, newTotKm):
        totKm = newTotKm

    def setPrice(self, price):
        self.price = price
    def setColor(self, color):
        self.color = color

class Ford(Car):
    def __init__(self):
        print "Balls."

    def breakLvl(self):
        print "car's break lvl is %s"% Car.breakLvl


f = Ford()
f.breakLvl()
f.setTotKm(200)
f.setColor("blue")
f.getColor()
f.getTotKm()

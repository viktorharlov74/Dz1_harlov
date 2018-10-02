from random import randint
class Auto:
    def __init__(self, name, max_speed,drag_coef,time_to_max):
        self.name = name
        self.max_speed = max_speed
        self.drag_coef = drag_coef
        self.time_to_max = time_to_max

    def start(self):
        print(self.name)

class Weather:

    def __init__(self, wind):
        self.wind =randint(0, wind)
        
    def start(self):
        print(self.wind)

        
class Tournament:
    competitor_time = 0
    competitor_speed = 0
    res={}
    cars=[]
    ferrary=Auto("ferrary",340, 0.324, 26)
    bugatti=Auto("bugatti",407, 0.39, 32)
    toyota=Auto("toyota",180, 0.24, 36)
    lada=Auto("lada",120, 0.54, 76)
    sx4=Auto("sx4",176, 0.384, 26)
    cars=[ferrary,bugatti,toyota,lada,sx4]
    weather=Weather(20)
    
    def __init__(self,distance):
        self.distance=distance
        
    def start(self):
        for auto in self.cars:
            self.competitor_time = 0
            self.competitor_speed = 0
            for dist in range(self.distance):
                if self.competitor_time == 0:
                    speed = 1
                else:
                    speed = (self.competitor_time / auto.time_to_max * auto.max_speed)
                    if speed > self.weather.wind:
                             speed-= (auto.drag_coef * self.weather.wind)
                self.competitor_time+= float(1) /speed
            self.res[auto.name]=self.competitor_time
    def finish(self):
        for car in self.res:
            print("Car <%s> result: %f" % (car, self.res[car]))


tur=Tournament(1000)
tur.start()
tur.finish()
#31
class Robot:
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy

    def work(self):
        if self.energy > 0:
            print("Robot ishlayapti")
        else:
            print("Energiya yo‘q")


r1 = Robot("Robo", 10)
r1.work()


#32
class Pet:
    def __init__(self, name, hunger):
        self.name = name
        self.hunger = hunger

    def feed(self):
        print(f"{self.name} to‘yindi")


p = Pet("Tom", 5)
p.feed()


#33
class Delivery:
    def __init__(self, status):
        self.status = status

    def check(self):
        if self.status:
            print("Yetkazildi")
        else:
            print("Yo‘lda")


d = Delivery(True)
d.check()


#34
class Quiz:
    def __init__(self, correct):
        self.correct = correct

    def result(self):
        if self.correct == 5:
            print("O‘tdingiz")
        else:
            print("Yiqildingiz")


q = Quiz(5)
q.result()
q = Quiz(5)
q.result()


#35
class WeatherApp:
    def __init__(self, weather):
        self.weather = weather

    def show(self):
        print(f"Bugun {self.weather}")


w = WeatherApp("yomg‘ir")
w.show()

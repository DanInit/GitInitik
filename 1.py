class Сar:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color

    def action(self):
        return f"Smth"


class Bmw(Сar):
    def action(self):
        return f"{self.color} она черная!"


class Tesla(Сar):
    def action(self):
        return f"{self.color} она белая!"


bmw = Bmw("fast" ,"black")
print(bmw.action())

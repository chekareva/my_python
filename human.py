class Human:
    def __init__(self,petr):
        print('Родился человек c именем: ')
        self.name=petr
        print(self.name,"отмечает день рождения")

    def eating(self):
        print(self.name,"ест")

    def sleeping(self):
        print(self.name,"спит")

    def working(self):
        print(self.name,"работает")

    def relaxing(self):
        print(self.name,"отдыхает")

    def pension(self):
        print(self.name, "на пенсии")

    def growing(self):
        print(self.name, "на год ближе к смерти")

class Life:
    def life(self, human, years=70):
        while years:
            human.growing()
            human.eating()
            human.sleeping()
            if 53>=years and years>5:
                human.working()
            if 5<=years:
                human.pension()
                human.relaxing()
                years -= 1
    return(print("Умер"))
petr = Human('Петр')
life_petr = Life()
life_petr.life(petr)

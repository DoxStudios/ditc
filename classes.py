class Barbarian:
    def __init__(self):
        self.damageMultipliers = {
            "melee": 2,
            "ranged": 0.5,
            "spell": 0.25
        }

        self.defense = {
            "melee": 0.25,
            "ranged": 0.5,
            "spell": 1.25
        }

        self.healthBuff = 20
        self.hungerBuff = 0
        self.sanityBuff = -20

class Temp:
    def __init__(self):
        self.damageMultipliers = {
            "melee": 2,
            "ranged": 0.5,
            "spell": 0.25
        }

        self.defense = {
            "melee": 0.25,
            "ranged": 0.5,
            "spell": 1.25
        }

        self.healthBuff = 20
        self.hungerBuff = 0
        self.sanityBuff = -20

class Temp2:
    def __init__(self):
        self.damageMultipliers = {
            "melee": 2,
            "ranged": 0.5,
            "spell": 0.25
        }

        self.defense = {
            "melee": 0.25,
            "ranged": 0.5,
            "spell": 1.25
        }

        self.healthBuff = 20
        self.hungerBuff = 0
        self.sanityBuff = -20





class ClassManager:
    def __init__(self):
        self.classes = {
            "1": Barbarian(),
            "2": Temp(),
            "3": Temp2()
        }
        

    def getClass(self, classNumber):
        return self.classes[str(classNumber)]
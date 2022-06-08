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
        self.addedDamage = 10

class Archer:
    def __init__(self):
        self.damageMultipliers = {
            "melee": 0.75,
            "ranged": 1.5,
            "spell": 0.25
        }

        self.defense = {
            "melee": 1,
            "ranged": 0,
            "spell": 1.25
        }

        self.healthBuff = 0
        self.hungerBuff = 20
        self.sanityBuff = 20
        self.addedDamage = 5

class Wizard:
    def __init__(self):
        self.damageMultipliers = {
            "melee": 0,
            "ranged": 0,
            "spell": 10
        }
        
        self.defense = {
            "melee": 2,
            "ranged": 2,
            "spell": 0
        }

        self.healthBuff = -20
        self.hungerBuff = 0
        self.sanityBuff = 50
        self.addedDamage = 0


class ClassManager:
    def __init__(self):
        self.classes = {
            1: Barbarian(),
            2: Archer(),
            3: Wizard()
        }


    def getClass(self, classNumber):
        return self.classes[classNumber]

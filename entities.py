from tabnanny import check


class Player:
    def __init__(self, name="Player", health=100, hunger=100, sanity=100, damageMultipliers={"melee": 1, "ranged": 1, "spell": 1}, additionalDamage=0, defense={"melee": 1, "ranged": 1, "spell": 1}, currentScreen="Main Menu", canEncounter=False, weaponInventory=[], petInventory=[], checkPoints=[]):
        self.name = name
        self.health = health
        self.hunger = hunger
        self.sanity = sanity
        self.damageMultipliers = damageMultipliers
        self.additionalDamage = additionalDamage
        self.defense = defense
        self.currentScreen = currentScreen
        self.canEncounter = canEncounter
        self.weaponInventory = weaponInventory
        self.petInventory = petInventory
        self.checkPoints = checkPoints

    def damage(self, damage, damageType):
        self.health -= damage * self.defenseValues[damageType]

    def getCard(self):
        card = f"Character Name: {self.name}\n\nHealth: {self.health}\n\nHunger: {self.hunger}\n\nSanity {self.sanity}\n"
        return card

    def getInventoryForSaving(self):
        weapons = self.weaponInventory
        pets = self.petInventory

        weapons = [i.id for i in weapons]
        pets = [i.id for i in pets]

        return (weapons, pets)

    def getStats(self):
        weaponNames, petNames = self.getInventoryForSaving()
        stats = {
            "name": self.name,
            "health": self.health,
            "hunger": self.hunger,
            "sanity": self.sanity,
            "damage multipliers": self.damageMultipliers,
            "added damage": self.additionalDamage,
            "defense multipliers": self.defense,
            "current screen": self.currentScreen,
            "can encounter": self.canEncounter,
            "weapon inventory": weaponNames,
            "pet inventory": petNames,
            "check points": self.checkPoints
        }

        return stats

class EntityManager:

    def __init__(self):
        self.player = Player()

    def createPlayerEntity(self, name="Player", health=100, hunger=100, sanity=100, damageMultipliers={"melee": 1, "ranged": 1, "spell": 1}, additionalDamage=0, defense={"melee": 1, "ranged": 1, "spell": 1}, currentScreen="Main Menu", canEncounter=False, weaponInventory=[], petInventory=[], checkPoints=[]):
        player = Player(name, health, hunger, sanity, damageMultipliers, additionalDamage, defense, currentScreen, canEncounter, weaponInventory, petInventory, checkPoints)
        return player
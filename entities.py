class Entity:
    def __init__(self, name, health, hunger, sanity, damageMultipliers, defense, currentScreen, weaponInventory, petInventory):
        self.name = name
        self.health = health
        self.hunger = hunger
        self.sanity = sanity
        self.damageMultipliers = damageMultipliers
        self.defense = defense
        self.currentScreen = currentScreen
        self.weaponInventory = weaponInventory
        self.petInventory = petInventory

    def damage(self, damage, damageType):
        self.health -= damage * self.defenseValues[damageType]

class Player(Entity):
    def getCard(self):
        card = f"Character Name: {self.name}\n\nHealth: {self.health}\n\nHunger: {self.hunger}\n\nSanity {self.sanity}\n"
        return card

    def getInventoryForSaving(self):
        weapons = self.weaponInventory
        pets = self.petInventory

        weapons = [i.name for i in weapons]
        pets = [i.name for i in pets]

        return (weapons, pets)

    def getStats(self):
        weaponNames, petNames = self.getInventoryForSaving()
        stats = {
            "name": self.name,
            "health": self.health,
            "hunger": self.hunger,
            "sanity": self.sanity,
            "damage multipliers": self.damageMultipliers,
            "defense multipliers": self.defense,
            "current screen": self.currentScreen,
            "weapon inventory": weaponNames,
            "pet inventory": petNames
        }

        return stats


class EntityManager:

    def __init__(self):
        self.player = Player("Player", 100, 100, 100, {"melee": 1, "ranged": 1, "spell": 1}, {"melee": 1, "ranged": 1, "spell": 1}, "Catacombs Entrance", [], [])

    def createPlayerEntity(self, name, health, hunger, sanity, damageMultipliers, defense, currentScreen, weaponInventory, petInventory):
        player = Player(name, health, hunger, sanity, damageMultipliers, defense, currentScreen, weaponInventory, petInventory)
        return player
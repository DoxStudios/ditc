class Item:
    def __init__(self, name, canHaveMultiple=True, damage=None, damageType=None):
        self.name = name
        self.canHaveMultiple = canHaveMultiple
        self.damage = damage
        self.damageType = damageType

class ItemManager:
    def __init__(self):
        self.Items = {
            "Rusty Knife": Item("Rusty Knife", damage=2, damageType="melee"),
            "Silver Sword": Item("Silver Sword", damage=5, damageType="melee")
        }

        self.Pets = {
            "Dark Sludge": Item("Dark Sludge", False)
        }

class InventoryManager:
    def __init__(self, EntityManager):
        self.entityManager = EntityManager
        self.itemManager = ItemManager()

    def getWeaponInventory(self):
        return self.entityManager.player.weaponInventory

    def getWeapons(self):
        weapons = [f"Slot {i + 1}: {self.getWeaponInventory()[i].name} - {self.getWeaponInventory()[i].damage} damage" for i in range(len(self.getWeaponInventory()))]
        
        if len(weapons) == 0:
            return "None\n"
        
        card = ""
        for i in weapons:
            card += i + "\n"

        return card

    def getPetInventory(self):
        return self.entityManager.player.petInventory

    def getPets(self):
        pets = [f"Slot {i + 1}: {self.getPetInventory()[i].name}" for i in range(len(self.getPetInventory()))]

        if len(pets) == 0:
            return "None\n"

        card = ""
        for i in pets:
            card += i + "\n"

        return card

    def addWeapon(self, itemName):
        weaponInventory = self.getWeaponInventory()
        item = self.itemManager.Items[itemName]
        if item.canHaveMultiple:
            weaponInventory.append(item)
        else:
            if not item in weaponInventory:
                weaponInventory.append(item)

    def addPet(self, petName):
        petInvetory = self.getPetInventory()
        pet = self.itemManager.Pets[petName]
        if pet.canHaveMultiple:
            petInvetory.append(pet)
        else:
            if not pet in petInvetory:
                petInvetory.append(pet)
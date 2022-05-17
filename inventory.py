class Item:
    def __init__(self, name, canHaveMultiple):
        self.name = name
        self.canHaveMultiple = canHaveMultiple

class ItemManager:
    def __init__(self):
        self.Items = {
            "Item": Item("Item", True)
        }

        self.Pets = {
            "Pet": Item("Pet", False)
        }

class InventoryManager:
    def __init__(self, EntityManager):
        self.entityManager = EntityManager
        self.itemManager = ItemManager()

    def getWeaponInventory(self):
        return self.entityManager.player.weaponInventory

    def getWeapons(self):
        weapons = [f"Slot {i + 1}: {self.getWeaponInventory()[i].name}" for i in range(len(self.getWeaponInventory()))]
        card = ""
        for i in weapons:
            card += i + "\n"

        return card

    def getPets(self):
        pets = [f"Slot {i + 1}: {self.getPetInventory()[i].name}" for i in range(len(self.getPetInventory()))]
        card = ""
        for i in pets:
            card += i + "\n"

        return card
        
    
    def getPetInventory(self):
        return self.entityManager.player.petInventory

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
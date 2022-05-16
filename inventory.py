class Item:
    def __init__(self, name, canHaveMultiple):
        self.name = name
        self.canHaveMultiple = canHaveMultiple

class ItemManager:
    def __init__(self):
        self.Items = {
            "Item": Item("Item", True),
            "Item2": Item("Item but better", False)
        }

class InventoryManager:
    def __init__(self, EntityManager):
        self.entityManager = EntityManager
        self.itemManager = ItemManager()

    def getWeaponInventory(self):
        return self.entityManager.player.weaponInventory
    
    def getPetInventory(self):
        return self.entityManager.player.petInventory

    def addWeapon(self, itemName):
        weaponInventory = self.getWeaponInventory()
        item = self.itemManager.Items[itemName]
        if item.canHaveMultiple:
            weaponInventory.append(item)
        else:
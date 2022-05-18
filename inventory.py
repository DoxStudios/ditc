class Item:
    def __init__(self, name, id, canHaveMultiple, damage, damageType):
        self.name = name
        self.id = id
        self.canHaveMultiple = canHaveMultiple
        self.damage = damage
        self.damageType = damageType

class ItemManager:
    def __init__(self):
        self.Items = {
            "rusty_knife": Item("Rusty Knife", "rusty_knife", True, 2, "melee"),
            "silver_sword": Item("Silver Sword", "silver_sword", True, 5, "melee"),
            "glowing_sword": Item("Glowing Sword", "glowing_sword", True, 9, "melee"),
            "shiny_dagger": Item("Shiny Dagger", "shiny_dagger", True, 4, "melee")
        }

        self.Pets = {
            "dark_sludge_pet": Item("Dark Sludge Pet", "dark_sludge_pet", False, 2, "spell"),
            "dox_pet": Item("Dox Pet", "dox_pet", False, 3, "ranged"),
            "dragon_fruit_pet": Item("Dragon Fruit Pet", "dragon_fruit_pet", False, 8, "static"),
            "spirit_pet": Item("Spirit Pet", "spirit_pet", False, 4, "spell")
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

    def getWeaponName(self, id):
        return self.itemManager.Items[id].name

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

    def getPetName(self, id):
        return self.itemManager.Pets[id].name

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
import json
from inputs import clear

class Screen:
    def __init__(self, prompt, options, InputManager, ClassManager, EntityManager, InventoryManager):
        self.prompt = prompt
        self.options = options
        self.InputManager = InputManager
        self.ClassManager = ClassManager
        self.EntityManager = EntityManager
        self.InventoryManager = InventoryManager

    def run(self):
        print("This screen hasn't been properly configured! This should be fixed soon.")

    def settings(self, previousScreen):
        clear()
        selection = self.InputManager.getInput("Options", ["1: Save", "2: View Inventory", "3: Go To Main Menu", "4: Go Back"])
        if selection == 1:
            self.saveCharacter()
            return previousScreen
        if selection == 2:
            self.viewInventory()
            return previousScreen
        if selection == 3:
            return "Main Menu"
        if selection == 4:
            return previousScreen

    def saveCharacter(self):
        playerData = self.EntityManager.player.getStats()
        with open(self.EntityManager.player.name.lower() + ".json", 'w') as saveFile:
            json.dump(playerData, saveFile)
        
    def createCharacter(self):
        clear()
        playerName = input("Enter a name for your character\n")
        clear()
        playerClass = self.ClassManager.getClass(self.InputManager.getInput("Please Select A Class", ["1: Barabarian", "2: Archer", "3: Temp"]))
        player = self.EntityManager.createPlayerEntity(playerName, 100 + playerClass.healthBuff, 100 + playerClass.hungerBuff, 100 + playerClass.sanityBuff, playerClass.damageMultipliers, playerClass.defense, "Catacombs Entrance", False, [], [])
        self.EntityManager.player = player
        return player.currentScreen

    def getCharacterName(self):
        clear()
        selection = self.InputManager.getInput("Character Selection", ["1: Enter A Character's Name", "3: Go Back"])
        if selection == 1:
            return self.loadCharacter()
        if selection == 2:
            return self.run()

    def loadCharacter(self):
        clear()
        characterName = input("Enter your character's name\n")
        try:
            with open(characterName.lower() + '.json', 'r') as saveFile:
                saveData = json.load(saveFile)
            player = self.EntityManager.createPlayerEntity(saveData["name"], saveData["health"], saveData["hunger"], saveData["sanity"], saveData["damage multipliers"], saveData["defense multipliers"], saveData["current screen"], saveData["can encounter"], [], [])
            self.EntityManager.player = player
            for i in saveData["weapon inventory"]:
                self.InventoryManager.addWeapon(i)
            for i in saveData["pet inventory"]:
                self.InventoryManager.addPet(i)
            return player.currentScreen
            
        except:
            print("That character does not exist or contains invalid data.")
            self.InputManager.pause()
            return self.getCharacterName()

    def viewInventory(self):
        clear()
        print("Weapons:")
        print(self.InventoryManager.getWeapons())
        print("Pets:")
        print(self.InventoryManager.getPets())
        self.InputManager.pause()



class MainMenu(Screen):
    def run(self):
        clear()
        selection = self.InputManager.getInput(self.prompt, self.options)
        if selection == 1:
            return self.createCharacter()
        if selection == 2:
            return self.getCharacterName()
        if selection == 3:
            clear()
            exit()

        
class CatacombsEntrance(Screen):
    def run(self):
        selection = self.InputManager.getInput(self.prompt, self.options)
        if selection == 1:
            return "Left Tunnel"
        if selection == 2:
            return "Right Tunnel"
        if selection == 3:
            return self.settings("Catacombs Entrance")

class LeftTunnel(Screen):
    def run(self):
        selection = self.InputManager.getInput(self.prompt, self.options)
        if selection == 1:
            self.InputManager.printResult("You attack the goblin and defeat it, but you decide to retread back to the entrance.")
            return "Catacombs Entrance"
        if selection == 2:
            self.InputManager.printResult("You sneak around the goblin and continue on your way.")
            return "Dark Room"
        if selection == 3:
            return self.settings("Left Tunnel")

class RightTunnel(Screen):
    def run(self):
        selection = self.InputManager.getInput(self.prompt, self.options)
        if selection == 1:
            self.InputManager.printResult("You go around the tomb and continue on your way.")
            return "Dark Room"
        if selection == 2:
            self.InventoryManager.addWeapon("Rusty Knife")
            self.InputManager.printResult("You find a Rusty Knife and go around the tomb.")
            return "Dark Room"
        if selection == 3:
            return self.settings("Right Tunnel")

class DarkRoom(Screen):
    def run(self):
        selection = self.InputManager.getInput(self.prompt, self.options)
        if selection == 1:
            return "Library"
        if selection == 2:
            return "Living Chambers"
        if selection == 3:
            return "Goblin Hideout"
        if selection == 4:
            return self.settings("Dark Room")

class Library(Screen):
    def run(self):
        selection = self.InputManager.getInput(self.prompt, self.options)
        if selection == 1:
            self.EntityManager.player.canEncounter = True
            self.InputManager.printResult("You read the forbidden book, and discover the secrets to fighting any enemy (more possible enemies to encounter), you then conitnue out of the room.")
            return "Plant Room"
        if selection == 2:
            self.InputManager.printResult("You open the ancient book, but a mysterious force closes it and pushes you out of the room.")
            return "Dark Room"
        if selection == 3:
            return self.settings("Library")

class GoblinHideout(Screen):
    def run(self):
        selection = self.InputManager.getInput(self.prompt, self.options)
        if selection == 1:
            self.InventoryManager.addWeapon("Silver Sword")
            self.InputManager.printResult("You go into the treasure room and find a large number of chests. You open one and find a Silver Sword. You then continue on your way.")
            return "Plant Room"
        if selection == 2:
            return "Plant Room"
        if selection == 3:
            return self.settings("Goblin Hideout")

class LivingChambers(Screen):
    def run(self):
        selection = self.InputManager.getInput(self.prompt, self.options)
        if selection == 1:
            self.InputManager.printResult("Your fists go right through the monster, but it seems to not notice.")
            return "Living Chambers"
        if selection == 2:
            self.InputManager.printResult("You retreat without it noticing you and end up back in the dark room.")
            return "Dark Room"
        if selection == 3:
            self.InventoryManager.addPet("Dark Sludge")
            self.InputManager.printResult("After slaying the dark creature you see a small show block wants to join you. You pick it up and it begins flaoting along with you. You continue along your way.")
            return "Plant Room"
        if selection == 4:
            return self.settings("Living Chambers")

class PlantRoom(Screen):
    def run(self):
        selection = self.InputManager.getInput(self.prompt, self.options)
        if selection == 1:
            return "Chest Room"
        if selection == 2:
            return "Experiment Room"
        if selection == 3:
            return "Crack In Wall"
        if selection == 4:
            return self.settings("Plant Room")


class ScreenManager:
    def __init__(self, InputManager, ClassManager, EntityManager, InventoryManager):
        
        self.InputManager = InputManager
        self.ClassManager = ClassManager
        self.EntityManager = EntityManager
        self.InventoryManager = InventoryManager

        self.screens = {
            "Main Menu": MainMenu("Main Menu", ["1: Create Character", "2: Load Character", "3: Exit"], self.InputManager, self.ClassManager, self.EntityManager, self.InventoryManager),
            "Catacombs Entrance": CatacombsEntrance("Catacombs Entrance", ["1: Enter catacombs through left tunnel", "2: Enter catacombs through right tunnel", "3: Options"], self.InputManager, self.ClassManager, self.EntityManager, self.InventoryManager),
            "Left Tunnel": LeftTunnel("You go down the left tunnel and encounter a goblin", ["1: Fight goblin", "2: Avoid goblin", "3: Options"], self.InputManager, self.ClassManager, self.EntityManager, self.InventoryManager),
            "Right Tunnel": RightTunnel("You go down right tunnel and find your path blocked by a tomb.", ["1: Go around", "2: Loot", "3: Options"], self.InputManager, self.ClassManager, self.EntityManager, self.InventoryManager),
            "Dark Room": DarkRoom("You find youself in a dark room. The dark room has three doors, labeled library, living chambers, and the final one is in a text you cannot read.", ["1: Go to library", "2: Go to living chambers", "3: Go down unknown path", "4: Options"], self.InputManager, self.ClassManager, self.EntityManager, self.InventoryManager),
            "Library": Library("Now in the library you look through the shelves, but most of them are empyty. You find two books, one labeled the Forbidden Book, and one with no label, that appears to be ancient.", ["1: Read forbidden book", "2: Read ancient book", "3: Options"], self.InputManager, self.ClassManager, self.EntityManager, self.InventoryManager),
            "Goblin Hideout": GoblinHideout("You find yourself in a large area with lots of path to explore.", ["1: Loot", "2: Continue through the room", "3: Options"], self.InputManager, self.ClassManager, self.EntityManager, self.InventoryManager),
            "Living Chambers": LivingChambers("You enter the living chambers and find a dark creature seemingly made of shadows. You must act fast before it notices you.", ["1: Attack with your fists", "2: Retreat before it notices you", "3: Sneak attack", "4: Options"], self.InputManager, self.ClassManager, self.EntityManager, self.InventoryManager),
            "Plant Room": PlantRoom("You find yourself in a room overgrown with plants. There are two small room attached, one labeled Chest Room, and one labeled Experiment Room. You also notice a small crack in the wall, barely big enough to fit through, that eads to darkness.", ["1: Enter Chest Room", "2: Enter Experiment Room", "3: Enter crack in the wall", "4: Options"], self.InputManager, self.ClassManager, self.EntityManager, self.InventoryManager)
        }

    def runScreen(self, screenName):
        return self.screens[screenName].run()

    def clear(self):
        clear()
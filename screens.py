import json
import os
from select import select

def clear():
    os.system(['clear','cls'][os.name == 'nt'])

class Screen:
    def __init__(self, prompt, options, InputManager, ClassManager, EntityManager):
        self.prompt = prompt
        self.options = options
        self.InputManager = InputManager
        self.ClassManager = ClassManager
        self.EntityManager = EntityManager

    def run(self):
        print("This screen hasn't been properly configured! This should be fixed soon.")

    def options(self, previousScreen):
        clear()
        selection = self.InputManager.getInput("Options", ["1: Save", "2: Go To Main Menu", "3: Go Back"])
        if selection == 1:
            return self.saveCharacter(previousScreen)
        if selection == 2:
            return "Main Menu"
        if selection == 3:
            return previousScreen

    def saveCharacter(self, previousScreen):
        playerData = self.EntityManager.player.getStats()
        with open(self.EntityManager.player.name.lower() + ".json", 'w') as saveFile:
            json.dump(playerData, saveFile)
        return self.options(previousScreen)

    def createCharacter(self):
        clear()
        playerName = input("Enter a name for your character\n")
        clear()
        playerClass = self.ClassManager.getClass(self.InputManager.getInput("Please Select A Class", ["1: Barabarian", "2: Archer", "3: Temp"]))
        player = self.EntityManager.createPlayerEntity(playerName, 100 + playerClass.healthBuff, 100 + playerClass.hungerBuff, 100 + playerClass.sanityBuff, playerClass.damageMultipliers, playerClass.defense, "Catacombs Entrance")
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
            player = self.EntityManager.createPlayerEntity(saveData["name"], saveData["health"], saveData["hunger"], saveData["sanity"], saveData["damage multipliers"], saveData["defense multipliers"], saveData["current screen"])
            self.EntityManager.player = player
            return player.currentScreen
            
        except:
            print("That character does not exist or contains invalid data.")
            self.InputManager.pause()
            return self.getCharacterName()



class MainMenu(Screen):
    def run(self):
        clear()
        selection = self.InputManager.getInput(self.prompt, self.options)
        if selection == 1:
            return self.createCharacter()
        if selection == 2:
            return self.getCharacterName()
        if selection == 3:
            exit()

        
class CatacombsEntrance(Screen):
    def run(self):
        selection = self.InputManager.getInput(self.prompt, self.options)
        if selection == 1:
            return "Left Tunnel"
        if selection == 2:
            return "Right Tunnel"
        if selection == 3:
            return self.options("Catacombs Entrance")

class LeftTunnel(Screen):
    def run(self):
        selection = self.InputManager.getInput(self.prompt, self.options)
        if selection == 1:
            self.InputManager.printResult("You attack the goblin and defeat it, but you decide to retread back to the entrance.")
            
            return "Catacombs Entrance"
        if selection == 2:
            self.InputManager.printResult("You sneak around the goblin and continue on your way.")
            self.InputManager.pause()
            return "Dark Room"
        if selection == 3:
            return self.options("Left Tunnel")

class RightTunnel(Screen):
    def run(self):
        selection = self.InputManager.getInput(self.prompt, self.options)

class ScreenManager:
    def __init__(self, InputManager, ClassManager, EntityManager):
        
        self.InputManager = InputManager
        self.ClassManager = ClassManager
        self.EntityManager = EntityManager

        self.screens = {
            "Main Menu": MainMenu("Main Menu", ["1: Create Character", "2: Load Character", "3: Exit"], self.InputManager, self.ClassManager, self.EntityManager),
            "Catacombs Entrance": CatacombsEntrance("Catacombs Entrance", ["1: Enter catacombs through left tunnel", "2: Enter catacombs through right tunnel", "3: Options"], self.InputManager, self.ClassManager, self.EntityManager),
            "Left Tunnel": LeftTunnel("You go down the left tunnel and encounter a goblin", ["1: Fight goblin", "2: Avoid goblin", "3: Options"], self.InputManager, self.ClassManager, self.EntityManager),
            "Right Tunnel": RightTunnel("You go down right tunnel and find your path blocked by a tomb.", ["1: Go around", "2: Loot", "3: Options"], self.InputManager, self.ClassManager, self.EntityManager)
        }

    def runScreen(self, screenName):
        return self.screens[screenName].run()

    def clear(self):
        clear()
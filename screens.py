import json
import os

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

    def settings(self):
        clear()
        selection = self.InputManager.getInput("Settings", ["1: Save"])
        if selection == 1:
            self.saveCharacter()

    def saveCharacter(self):
        playerData = self.EntityManager.player.getStats()
        with open(self.EntityManager.player.name.lower() + ".json", 'w') as saveFile:
            json.dump(json.loads(playerData), saveFile)

    def createCharacter(self):
        clear()
        playerName = input("Enter a name for your character\n")
        clear()
        playerClass = self.ClassManager.getClass(self.InputManager.getInput("Please Select A Class", ["1: Barabarian", "2: Temp", "3: Temp"]))
        player = self.EntityManager.createPlayerEntity(playerName, 100 + playerClass.healthBuff, 100 + playerClass.hungerBuff, 100 + playerClass.sanityBuff, playerClass.damageMultipliers, playerClass.defense, "Catacombs Entrance")
        return player

    def getCharacterName(self):
        clear()
        selection = self.InputManager.getInput("Character Selection", ["1: Enter A Character's Name", "2: Go Back"])
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
            return player
            
        except:
            print("That character does not exist or contains invalid data.")
            input("Press Enter To Continue")
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
            self.settings()
            return "Catacombs Entrance"

class ScreenManager:
    def __init__(self, InputManager, ClassManager, EntityManager):
        
        self.InputManager = InputManager
        self.ClassManager = ClassManager
        self.EntityManager = EntityManager

        self.screens = {
            "Main Menu": MainMenu("Main Menu", ["1: Create Character", "2: Load Character", "3: Exit"], self.InputManager, self.ClassManager, self.EntityManager),
            "Catacombs Entrance": CatacombsEntrance("Catacombs Entrance", ["1: Enter catacombs through left tunnel", "2: Enter catacombs through right tunnel", "3: Settings"], self.InputManager, self.ClassManager, self.EntityManager)
        }

    def runScreen(self, screenName):
        return self.screens[screenName].run()

    def clear(self):
        clear()
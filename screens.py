import json
import random
from re import L
from inputs import clear

def chance(percent):
    if random.randint(0, 100) < percent:
        return True
    else:
        return False

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
        player = self.EntityManager.createPlayerEntity(playerName, 100 + playerClass.healthBuff, 100 + playerClass.hungerBuff, 100 + playerClass.sanityBuff, playerClass.damageMultipliers, playerClass.addedDamage, playerClass.defense, "Catacombs Entrance", False, [], [], [])
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
            player = self.EntityManager.createPlayerEntity(saveData["name"], saveData["health"], saveData["hunger"], saveData["sanity"], saveData["damage multipliers"], saveData["added damage"], saveData["defense multipliers"], saveData["current screen"], saveData["can encounter"], [], [], saveData["check points"])
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
            self.InventoryManager.addWeapon("rusty_knife")
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
            self.InventoryManager.addWeapon("silver_sword")
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

class ChestRoom(Screen):
    def run(self):
        selection = self.InputManager.getInput(self.prompt, self.options)
        if selection == 1:
            clear()
            self.EntityManager.player.canEncounter = False
            choice = self.InputManager.getInput("Opening chest 1 you find a bottle with a strange sludge (removes effects of reading forbidden book), when leaving, you notice a hidden door in the wall.", ["1: Investigate", "2: Ignore"])
            if choice == 1:
                return "Broken Chest Room"
            if choice == 2:
                return "Plant Room"
        if selection == 2:
            clear()
            choice = self.InputManager.getInput("When you try to open the chest, it leaps towards you and trys to attack you.", ["1: Attack it", "2: Run away"])
            if choice == 1:
                self.EntityManager.player.additionalDamage += 2
                self.InputManager.printResult("You attack it and kill it, you now feel more confident with your abilities (+2 permanent damage), you find a passegway behind the chest and continue through it.")
                return "Village"
            if choice == 2:
                self.InputManager.printResult("You run away and end up back in the plant room.")
                return "Plant Room"
        if selection == 3:
            self.InventoryManager.addPet("Dox Pet")
            self.InputManager.printResult("Opening this chest you find a small white fox with deer horns napping in it. The Dox Pet joins you and becomes your friend.")
            return "Plant Room"
        if selection == 4:
            return "Plant Room"
        if selection == 5:
            return self.settings("Chest Room")

class BrokenChestRoom(Screen):
    def run(self):
        selection = self.InputManager.getInput(self.prompt, self.options)
        if selection == 1:
            self.InventoryManager.addPet("Dragon Fruit Pet")
            self.InputManager.printResult("When you open this chest you find what looks like a dragon fruit. Realizing you are starving, you try to eat it. When attempting to eat it, it unfolds into a small dragon with the patterns of a dragonfruit.")
            return "Broken Chest Room"
        if selection == 2:
            clear()
            choice = self.InputManager.getInput("When you start unlocking this chest it moves suddenly away and slides into the wall, revealing a hidden ladder.", ["1: Go down the ladder", "2: Walk away"])
            if choice == 1:
                self.InputManager.printResult("The ladder leads you down until there is a sudden and large drop. You drop down and end up in the cneter of a village right above a trapdoor leading downwards.")
                return "Village Center Trapdoor"
            if choice == 2:
                return "Broken Chest Room"
        if selection == 3:
            return "Chest Room"
        if selection == 4:
            return self.settings("Broken Chest Room")

class CrackInWall(Screen):
    def run(self):
        selection = self.InputManager.getInput(self.prompt, self.options)
        if selection == 1:
            self.InputManager.printResult("When you try to resist the darkness you can feel is sapping your energy until you can't resist anymore. Now with the darkness leading you, you hear a thungering roar before finding an exit and leaving the crack in the wall.")
            return "Dark Room"
        if selection == 2:
            self.InputManager.printResult("Letting the darkness lead you, you hear a thundering roar before finding your way out of the crack in the wall.")
            return "Dark Room"

class ExperimentRoom(Screen):
    def run(self):
        selection = self.InputManager.getInput(self.prompt, self.options)
        if selection == 1:
            clear()
            choice = self.InputManager.getInput("Opening the cabinets you find several empty glass bottles, and one with a small spirit traped inside.", ["1: Release the spirit (+ Spirit Pet)", "2: Keep the spirit trapped (+ Encounter possibilities)"])
            if choice == 1:
                self.InventoryManager.addPet("Spirit Pet")
                self.InputManager.printResult("You release the spirit and it joins you, You now get a better look and it is a small pale ghost. You continue out of the room.")
                return "Village"
            if choice == 2:
                self.EntityManager.player.canEncounter = True
                self.InputManager.printResult("You keep the spirit trapped and put the bottle back, then continue out of the room.")
                return "Village"
        if selection == 2:
            self.EntityManager.player.weaponInventory = []
            self.EntityManager.player.petInventory = []
            self.InputManager.printResult("Climbing the ladder a rock suddenly falls and slices your bad open, dropping all your loot. At the top of the ladder you exit and find youself in the catacombs entrance.")
            return "Catacombs Entrance"
        if selection == 3:
            return self.settings("Experiment Room")

class Village(Screen):
    def run(self):
        selection = self.InputManager.getInput(self.prompt, self.options)
        if selection == 1:
            return "Weaponsmith"
        if selection == 2:
            return "Pet Keeper"
        if selection == 3:
            self.EntityManager.player.checkPoints = ["1: Go to catacombs entrance", "2: Go to dark room", "3: Go to plant room", "4: Walk away", "5: Options"]
            return "Shady Alley Man"
        if selection == 4:
            return self.settings("Village")

class ShadyAlleyMan(Screen):
    def run(self):
        selection = self.InputManager.getInput(self.prompt, self.EntityManager.player.checkPoints)
        if selection == len(self.EntityManager.player.checkPoints) - 1:
            return "Village"
        if selection == len(self.EntityManager.player.checkPoints):
            return self.settings("Shady Alley Man")
        if selection == 1:
            return "Catacombs Entrance"
        if selection == 2:
            return "Dark Room"
        if selection == 3:
            return "Plant Room"

class Weaponsmith(Screen):
    def run(self):
        selection = self.InputManager.getInput(self.prompt, self.options)
        if selection == 1:
            if chance(40):
                self.InventoryManager.addWeapon("glowing_sword")
                self.InputManager.printResult("The weaponsmith agrees to give you the Glowing Sword to aid you on your journey. However, he promptly kicks you out before you can try to get more.")
                return "Village"
            else:
                self.InputManager.printResult("He does not giv eyou the sword and instead kicks you out.")
                return "Village"
        if selection == 2:
            if chance(50):
                self.InventoryManager.addWeapon("shiny_dagger")
                self.InputManager.printResult("You steal the dagger without him noticing, then immediately leave.")
                return "Village"
            else:
                self.InputManager.printResult("He catches you trying to steal the dagger and kicks you out.")
                return "Village"

class PetKeeper(Screen):
    def run(self):
        selection = self.InputManager.getInput(self.prompt, self.options)
        if selection == 1:
            pets = ["dark_sludge", "dox_pet", "dragon_fruit_pet", "spirit_pet"]
            pet = random.choice(pets)
            self.InventoryManager.addPet(pet)
            self.InputManager.printResult(f"You got a {self.InventoryManager.getPetName(pet)}")
            return "Village"
        if selection == 2:
            self.InputManager.printResult("You: Whats been going on in the village?")
            self.InputManager.printResult("Pet Kepper: There's been this kids around the village that no one likes.")
            self.InputManager.printResult("You: Wow I hate that kid")
            self.InputManager.printResult("Pet Keeper: Me too. We are now friends I decided.")

            self.InputManager.printResult("After befriending the pet keeper, she tells you about a trapdoor that leads to a secret level of the catacombs.")
            return "Village Center Trapdoor"
        if selection == 3:
            return self.settings("Pet Keeper")

class VillageCenterTrapdoor(Screen):
    def ruin(self):
        selection = self.InputManager.getInput(self.prompt, self.options)
        if selection == 1:
            return "Flooded Catacombs"
        if selection == 2:
            return "Village"
        if selection == 3:
            return self.settings("Flooded Catacombs")

class FloodedCatacombs(Screen):
    def run(self):
        #Currently unplanned. Will add input once we know what to do here.
        #selection = self.InputManager.getInput(self.prompt, self.options)

        self.InputManager.printResult("Going down the ladder you find a sign saying 'Path not finished go back' and you listen.")
        return "Village Center Trapdoor"

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
            "Plant Room": PlantRoom("You find yourself in a room overgrown with plants. There are two small room attached, one labeled Chest Room, and one labeled Experiment Room. You also notice a small crack in the wall, barely big enough to fit through, that eads to darkness.", ["1: Enter Chest Room", "2: Enter Experiment Room", "3: Enter crack in the wall", "4: Options"], self.InputManager, self.ClassManager, self.EntityManager, self.InventoryManager),
            "Chest Room": ChestRoom("In the chest room you find three chests.", ["1: Loot chest 1", "2: Loot chest 2", "3: Loot chest 3", "4: Return to the plant room", "5: Options"], self.InputManager, self.ClassManager, self.EntityManager, self.InventoryManager),
            "Broken Chest Room": BrokenChestRoom("Leving through the hidden door you find a part of the catacombs which has fallen into more disrepair. It seems to be a second chest room, identical but with only 2 chests.", ["1: Loot chest 1", "2: Loot chest 2", "3: Return to main chest room", "4: Options"], self.InputManager, self.ClassManager, self.EntityManager, self.InventoryManager),
            "Crack In Wall": CrackInWall("After sliding into the crack you find an empty room, when you try to leave you find that the crack is gone and you are in complete darkness. Sliding you hands against the entire room to find an exit, you find that there is none. Suddenly, the darkness begins to pull you.", ["1: Resist the darkness", "2: Follow the darkness"], self.InputManager, self.ClassManager, self.EntityManager, self.InventoryManager),
            "Experiment Room": ExperimentRoom("In the experiment room you see a ladder and many cabinets.", ["1: Open the cabinets", "2: Climb the ladder", "3: Options"], self.InputManager, self.ClassManager, self.EntityManager, self.InventoryManager),
            "Village": Village("You find yourself in what seems to be a village built into the tombs and walls of the catacombs. The village is filled with friendly-looking monsters.", ["1: Go to the weaponsmith", "2: Go to the pet keeper", "3: Talk to the shady man in the alley", "4: Options"], self.InputManager, self.ClassManager, self.EntityManager, self.InventoryManager),
            "Shady Alley Man": ShadyAlleyMan("I know my way around the catacombs better than anyone else. I can help you between the layers.", [], self.InputManager, self.ClassManager, self.EntityManager, self.InventoryManager),
            "Weaponsmith": Weaponsmith("You greet the weaponsmith and take a look around his shop.", ["1: Negotiate for a Glowing Sword, 40% chance for him to accept", "2: Steal a Shiny Dagger", "3: Options"], self.InputManager, self.ClassManager, self.EntityManager, self.InventoryManager),
            "Pet Keeper": PetKeeper("You go into the pet keeper's shop and say hello.", ["1: Get a random pet from the upper floors", "2: Befriend the pet keeper", "3: Options"], self.InputManager, self.ClassManager, self.EntityManager, self.InventoryManager),
            "Village Center Trapdoor": VillageCenterTrapdoor("You find yourself at a trapdoor in the center of the village.", ["1: Open the trapdoor and go down the ladder underneath", "2: Walk away into the village", "3: Options"], self.InputManager, self.ClassManager, self.EntityManager, self.InventoryManager),
            "Flooded Catacombs": FloodedCatacombs("", [], self.InputManager, self.ClassManager, self.EntityManager, self.InventoryManager)
        }

    def runScreen(self, screenName):
        return self.screens[screenName].run()

    def clear(self):
        clear()
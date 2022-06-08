import entities
import classes
import inputs
import screens
import inventory

running = True

inputManager = inputs.InputManager()
classManager = classes.ClassManager()
entityManager = entities.EntityManager()
inventoryManager = inventory.InventoryManager(entityManager)
screenManager = screens.ScreenManager(inputManager, classManager, entityManager, inventoryManager)

if screenManager.runScreen("Main Menu") == "":
    running = False

while running:
    player = entityManager.player
    screenManager.clear()
    if player.currentScreen == "":
        running = False
    else:
        player.currentScreen = screenManager.runScreen(player.currentScreen)
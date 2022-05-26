import entities
import classes
import inputs
import screens
import inventory

alive = True

inputManager = inputs.InputManager()
classManager = classes.ClassManager()
entityManager = entities.EntityManager()
inventoryManager = inventory.InventoryManager(entityManager)
screenManager = screens.ScreenManager(inputManager, classManager, entityManager, inventoryManager)

screenManager.runScreen("Main Menu")

while alive:
    player = entityManager.player
    screenManager.clear()
    player.currentScreen = screenManager.runScreen(player.currentScreen)    
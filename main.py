import entities
import classes
import inputs
import screens
import inventory
import mirrorscreens

alive = True

inputManager = inputs.InputManager()
classManager = classes.ClassManager()
entityManager = entities.EntityManager()
inventoryManager = inventory.InventoryManager(entityManager)
screenManager = screens.ScreenManager(inputManager, classManager, entityManager, inventoryManager)
mirrorScreenManager = mirrorscreens.ScreenManager(inputManager, classManager, entityManager, inventoryManager)

screenManager.runScreen("Main Menu")

while alive:
    player = entityManager.player
    screenManager.clear()
    if player.mirrored:
        player.currentScreen = mirrorScreenManager.runScreen(player.currentScreen)
    else:
        player.currentScreen = screenManager.runScreen(player.currentScreen)
        
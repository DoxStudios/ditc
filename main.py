import entities
import classes
import inputs
import screens

alive = True

inputManager = inputs.InputManager()
classManager = classes.ClassManager()
entityManager = entities.EntityManager()
screenManager = screens.ScreenManager(inputManager, classManager, entityManager)

screenManager.runScreen("Main Menu")

while alive:
    player = entityManager.player
    screenManager.clear()
    player.currentScreen = screenManager.runScreen(player.currentScreen)
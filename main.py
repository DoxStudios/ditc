import entities
import classes
import inputs
import screens

alive = True

inputManager = inputs.InputManager()
classManager = classes.ClassManager()
entityManager = entities.EntityManager()
screenManager = screens.ScreenManager(inputManager, classManager, entityManager)

player = screenManager.runScreen("Main Menu")

entityManager.player = player

while alive:
    screenManager.clear()
    player.currentScreen = screenManager.runScreen(player.currentScreen)
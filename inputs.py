import os
from getkey import getkey, keys

def clear():
    os.system(['clear','cls'][os.name == 'nt'])

class InputManager:
    def getInput(self, prompt, options):

        optionText = ""

        for i in options:
            optionText += i + "\n"
            if options.index(i) < len(options) - 1:
                optionText += "\n"

        print(prompt + "\n\n" + optionText)
        userInput = getkey()

        try:
            userInput = int(userInput)
        except:
            userInput = len(options) + 1

        if userInput == 0:
            userInput = len(options) + 1

        while not userInput <= len(options):
            clear()
            print("That is not a valid option. Please enter a number between 1 and ", len(options), "\n")
            self.pause()
            clear()
            print(prompt + "\n\n" + optionText)
            userInput = getkey()
            try:
                userInput = int(userInput)
            except:
                userInput = len(options) + 1

            if userInput == 0:
                userInput = len(options) + 1

        return userInput


    def printResult(self, message):
        clear()
        print(f"{message}\n")

    def pause(self):
        print("Press Any Key To Continue")
        getkey()
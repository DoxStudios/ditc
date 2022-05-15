import os

def clear():
    os.system(['clear','cls'][os.name == 'nt'])

class InputManager:
    def getInput(self, prompt, options):

        optionText = ""

        for i in options:
            optionText += i + "\n\n"

        optionText += "Enter Your Selection: "

        print(prompt, "\n")
        userInput = input(optionText)

        try:
            userInput = int(userInput)
        except:
            userInput = len(options) + 1

        while not userInput <= len(options):
            clear()
            print("That is not a valid option. Please enter a number between 1 and ", len(options), "\n")
            self.pause()
            clear()
            print(prompt, "\n")
            userInput = input(optionText)
            try:
                userInput = int(userInput)
            except:
                userInput = len(options) + 1

        return userInput


    def printResult(self, message):
        print(f"\n{message}\n")

    def pause(self):
        input("Press Enter To Continue")
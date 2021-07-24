#These are functions that I did not think fit a specific file

import json

#Basic function to save a json file
def saveJSONFile(fileName, data):
    with open(fileName, "w") as jsonFile:
        json.dump(data, jsonFile, indent=4)

#This is the logic used to figure out if a game is a valid choice for the setting
#
#   a is boolean value of if the setting is on or off
#   b is the condition assosiated with the setting
#   
#   a   |   b   | Result
#-------|-------|-------
#   0       0       1
#   0       1       1
#   1       0       0
#   1       1       1
#
#   This means the function only returns false if the setting is on and the condition for the setting is false
#
#After not looking at this project for a while I realize this is probably not needed
#   I was using it shorten the length of the line deciding if the game fit the current filter settings but
#   I probably just ended up making it seem more complicated
def settingGate(a, b):
    return not (a and not b)
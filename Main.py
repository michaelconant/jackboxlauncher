#Programmer Name:   ProjectCuriosity
#Version Number :   1.2.1
#Python Version :   3.9 (64 Bit)
#OS             :   Windows

from tkinter import *           #for tkinter GUI
from random import randrange    #for random numbers

import subprocess               #for launching the games

from Classes.CanvasPicture import *
from Classes.PictureButton import *
from Classes.Packs import *

from Screens.MainMenu import *
from Screens.SettingsMenu import *
from Screens.JsonErrorScreen import *
from Screens.NoGamesEnabledScreen import *

from functions import *

##############################################################
###############################   Window Settings            #
##############################################################

root = Tk()
root.title("Jackbox Game Launcher v1.2")        #Name of program window
try:
    root.iconbitmap('logo.ico')                 #Icon that shows at the top left
except:
    print("ERROR: Could not find logo.ico")
root.geometry("1280x720")                       #Default Resolution

##############################################################
###############################   Variables/Objects          #
##############################################################

FILE_NAME = "games.json"
SETTINGS_FILE_NAME = "general_settings.json"
DEFAULT_THEME_FILE_NAME = "default_theme.json"

packs = Packs(FILE_NAME, DEFAULT_THEME_FILE_NAME, SETTINGS_FILE_NAME)

##############################################################
###############################   Bind/Button Functions      #
##############################################################

def shiftPrev(event):
    shiftPrevCommand()
def shiftNext(event):
    shiftNextCommand()

def shiftPrevCommand():
    mainMenu.shiftPack(packs, -1)

    bindHoverLabel()

    if len(packs.data[packs.currentPack]['games']) > 1:
        root.bind('<Up>', moveUp)
        root.bind('<w>', moveUp)
        root.bind('<Down>', moveDown)
        root.bind('<s>', moveDown)
    else:
        root.unbind('<Up>')
        root.unbind('<w>')
        root.unbind('<Down>')
        root.unbind('<s>')
def shiftNextCommand():
    mainMenu.shiftPack(packs, 1)

    bindHoverLabel()

    if len(packs.data[packs.currentPack]['games']) > 1:
        root.bind('<Up>', moveUp)
        root.bind('<w>', moveUp)
        root.bind('<Down>', moveDown)
        root.bind('<s>', moveDown)
    else:
        root.unbind('<Up>')
        root.unbind('<w>')
        root.unbind('<Down>')
        root.unbind('<s>')

def moveUp(event):
    mainMenu.changeGame(packs, (packs.currentGame - 1) % len(packs.data[packs.currentPack]['games']))
def moveDown(event):
    mainMenu.changeGame(packs, (packs.currentGame + 1) % len(packs.data[packs.currentPack]['games']))

def homeButtonPressed():
    settingsMenu.forget()

    if len(packs.enabledIndexs):

        mainMenu.display(packs)
        mainMenu.updateColors(packs)

        if len(packs.enabledIndexs) > 1:
            root.bind('<Left>', shiftPrev)
            root.bind('<a>', shiftPrev)
            root.bind('<Right>', shiftNext)
            root.bind('<d>', shiftNext)

        if len(packs.data[packs.currentPack]['games']) > 1:
            root.bind('<Up>', moveUp)
            root.bind('<w>', moveUp)
            root.bind('<Down>', moveDown)
            root.bind('<s>', moveDown)
            bindHoverLabel()

    else:
        noGamesEnabledScreen.display()

def randomButtonPressed():
    #Calulate total games
    totalGames = 0
    randGameNum = randrange(packs.validGames)         #Generates a random number between 0 and totalGames used for the position of the random game

    if not packs.settings['currentPlayers'] and not packs.settings['likeWeight'] and not packs.settings['excludeDislikes']:
        for i in range(len(packs.enabledIndexs)):
            if randGameNum >= len(packs.data[packs.enabledIndexs[i]]['games']):
                randGameNum -= len(packs.data[packs.enabledIndexs[i]]['games'])     #subtract the number of games in the pack from the random number
            else:
                mainMenu.changePack(packs, packs.enabledIndexs[i])      #Changes the pack on screen to the index packs.enabledIndexs[i]
                mainMenu.changeGame(packs, randGameNum)                 #Uses what is left from the random number to set the position of the game being selected in the pack
                break
    else:
        for i in range(0, len(packs.enabledIndexs)):
            for j in range(len(packs.data[packs.enabledIndexs[i]]['games'])):
                game = packs.data[packs.enabledIndexs[i]]['games'][j]
                if settingGate(packs.settings['currentPlayers'], (packs.settings['currentPlayers'] >= game['playerMin']) and (packs.settings['currentPlayers'] <= game['playerMax'])):
                    if packs.settings['likeWeight']:
                        if game['like'] < 0 and not packs.settings['excludeDislikes']:
                            randGameNum -= packs.settings['dislikeValue']
                        elif game['like'] == 0:
                            randGameNum -= packs.settings['normalValue']
                        else:
                            randGameNum -= packs.settings['likeValue']
                    else:
                        randGameNum -= settingGate(packs.settings['excludeDislikes'], game['like'] >= 0)
                    if randGameNum < 0:
                        mainMenu.changePack(packs, packs.enabledIndexs[i])
                        mainMenu.changeGame(packs, j)
                        break
            else:
                continue
            break

        bindHoverLabel()


def playButtonPressed():
    subprocess.call(packs.data[packs.currentPack]['gamePath'])

def settingsButtonPressed():
    mainMenu.forget()
    noGamesEnabledScreen.forget()

    root.unbind('<Left>')
    root.unbind('<a>')

    root.unbind('<Right>')
    root.unbind('<d>')

    root.unbind('<Up>')
    root.unbind('<w>')

    root.unbind('<Down>')
    root.unbind('<s>')

    settingsMenu.display(packs)

def dislikeButtonPressed():
    if packs.data[packs.currentPack]['games'][packs.currentGame]['like'] < 0:
        packs.data[packs.currentPack]['games'][packs.currentGame]['like'] = 0
    else:
        packs.data[packs.currentPack]['games'][packs.currentGame]['like'] = -1
    mainMenu.updateLikeButtons(packs)
    saveJSONFile(FILE_NAME, packs.data)
    mainMenu.updateButtonStates(packs)

def likeButtonPressed():
    if packs.data[packs.currentPack]['games'][packs.currentGame]['like'] > 0:
        packs.data[packs.currentPack]['games'][packs.currentGame]['like'] = 0
    else:
        packs.data[packs.currentPack]['games'][packs.currentGame]['like'] = 1
    mainMenu.updateLikeButtons(packs)
    saveJSONFile(FILE_NAME, packs.data)
    mainMenu.updateButtonStates(packs)


def updateTempPlayers(num):
    settingsMenu.tempPlayers += num
    settingsMenu.updatePlayers()

def saveButtonPressed():
    packs.settings['defaultThemeEnabled'] = settingsMenu.defaultThemeFlag.get()
    packs.settings['currentPlayers'] = settingsMenu.tempPlayers
    packs.settings['likeWeight'] = settingsMenu.weightLikes.get()
    packs.settings['excludeDislikes'] = settingsMenu.excludeDislikes.get()

    for i in range(len(packs.data)):
        packs.data[i]['enabled'] = settingsMenu.checkButtonState[i].get()
        packs.data[i]['gamePath'] = settingsMenu.textEntrys[i].get()

    packs.updateEnabledIndexs()
    packs.updateValidGames()

    saveJSONFile(FILE_NAME, packs.data)
    saveJSONFile(DEFAULT_THEME_FILE_NAME, packs.defaultTheme)
    saveJSONFile(SETTINGS_FILE_NAME, packs.settings)


def hoverUpdatePosition(event, num):
    mainMenu.changeGame(packs, num)

def bindHoverLabel():
    for i in range(len(packs.data[packs.currentPack]['games'])):
        mainMenu.gameLabels[i].bind("<Enter>", lambda event, arg=i: hoverUpdatePosition(event, arg))

##############################################################
###############################   Display Screen/Menu        #
##############################################################

if len(packs.data):
    mainMenu = MainMenu(root)
    settingsMenu = SettingsMenu(root, packs)
    noGamesEnabledScreen = NoGamesEnabledScreen(root)

    mainMenu.settingsButton.button.config(command=settingsButtonPressed)
    mainMenu.randomButton.button.config(command=randomButtonPressed)
    mainMenu.playButton.button.config(command=playButtonPressed)
    mainMenu.leftButton.button.config(command=shiftPrevCommand)
    mainMenu.rightButton.button.config(command=shiftNextCommand)
    mainMenu.dislikeButton.button.config(command=dislikeButtonPressed)
    mainMenu.likeButton.button.config(command=likeButtonPressed)

    noGamesEnabledScreen.settingsButton.button.config(command=settingsButtonPressed)

    settingsMenu.homeButton.button.config(command=homeButtonPressed)
    settingsMenu.saveButton.button.config(command=saveButtonPressed)
    settingsMenu.minusPlayersButton.button.config(command=lambda:updateTempPlayers(-1))
    settingsMenu.plusPlayersButton.button.config(command=lambda:updateTempPlayers(1))

    root.bind('<Left>', shiftPrev)
    root.bind('<a>', shiftPrev)
    root.bind('<Right>', shiftNext)
    root.bind('<d>', shiftNext)

    if len(packs.data[packs.currentPack]['games']) > 1:
        root.bind('<Up>', moveUp)
        root.bind('<w>', moveUp)
        root.bind('<Down>', moveDown)
        root.bind('<s>', moveDown)

    if len(packs.enabledIndexs):
        mainMenu.display(packs)
        mainMenu.changePack(packs, packs.currentPack)
        mainMenu.updateColors(packs)
        bindHoverLabel()
    else:
        noGamesEnabledScreen.display()
        mainMenu.changePack(packs, 0)
else:
    jsonErrorScreen = JsonErrorScreen(root)
    jsonErrorScreen.display()

root.mainloop()
from tkinter import * 

import json

from functions import settingGate

class Packs:
    def __init__(self, gameDataFilePath, defaultThemeFilePath, settingsFilePath):
        self.data = []
        self.defaultTheme = []
        self.enabledIndexs = []
        self.validGames = 0
        self.CheckbuttonStates = []
        self.currentPack = -1
        self.currentGame = 0
        self.currentPlayers = 0
        self.FONTNAME = "Arial Bold"
        try:
            #If in the future I find it necessary to check if the file is valid check for the keys in the json data using .has_key(keyName)
            defaultThemeFile = open(defaultThemeFilePath,)
            self.defaultTheme = json.load(defaultThemeFile)
            defaultThemeFile.close()

            settingsFile = open(settingsFilePath,)
            self.settings = json.load(settingsFile)
            if self.settings['currentPlayers'] > 17:
                self.settings['currentPlayers'] = 16
            if self.settings['currentPlayers'] < 0:
                self.settings['currentPlayers'] = 0
            settingsFile.close()

            gameDataFile = open(gameDataFilePath,)
            self.data = json.load(gameDataFile)
            gameDataFile.close()

            i = 0
            for element in self.data[:]:
                if not len(element['games']):
                    self.data.remove(element)
                if element['enabled']:
                    self.CheckbuttonStates.append(IntVar(value=0))
                    self.currentPack = i
                else:
                    self.CheckbuttonStates.append(IntVar(value=0))

                i += 1

            self.updateEnabledIndexs()

        except:
            print("ERROR FINDING FILE - Packs.constructor : " + gameDataFilePath + " or " + defaultThemeFilePath + " or " + settingsFilePath)

    def updateEnabledIndexs(self):
        self.enabledIndexs.clear()

        for i in range(len(self.data)):
            if self.data[i]['enabled']:
                self.enabledIndexs.append(i)

    #calculates the total games that are valid with the current settings
    def updateValidGames(self):
        self.validGames = 0
        #if all settings are off do the simple and fast check
        if not self.settings['currentPlayers'] and not self.settings['likeWeight'] and not self.settings['excludeDislikes']:
            for i in range(0, len(self.enabledIndexs)):
                self.validGames += len(self.data[self.enabledIndexs[i]]['games'])
        else:
            for i in range(0, len(self.enabledIndexs)):
                for game in self.data[self.enabledIndexs[i]]['games']:
                    #if the current game is valid with the current settings add it to validGames
                    if settingGate(self.settings['currentPlayers'], self.settings['currentPlayers'] >= game['playerMin'] and self.settings['currentPlayers'] <= game['playerMax']):
                        #if the likeWeight settings is on add the weighted value to validGames, if not just add 1
                        if self.settings['likeWeight']:
                            if game['like'] > 0:
                                self.validGames += self.settings['likeValue']
                            elif game['like'] == 0:
                                self.validGames += self.settings['normalValue']
                            elif not self.settings['excludeDislikes']:
                                self.validGames += self.settings['dislikeValue']
                        else:
                            #increment by 1 unless exludeDislikes is enabled and the game is disliked
                            self.validGames += settingGate(self.settings['excludeDislikes'], game['like'] >= 0)
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

    def updateValidGames(self):
        self.validGames = 0
        if not self.settings['currentPlayers'] and not self.settings['likeWeight'] and not self.settings['excludeDislikes']:
            for i in range(0, len(self.enabledIndexs)):
                self.validGames += len(self.data[self.enabledIndexs[i]]['games'])
        else:
            for i in range(0, len(self.enabledIndexs)):
                for game in self.data[self.enabledIndexs[i]]['games']:
                    if settingGate(self.settings['currentPlayers'], self.settings['currentPlayers'] >= game['playerMin'] and self.settings['currentPlayers'] <= game['playerMax']):
                        if self.settings['likeWeight']:
                            if game['like'] > 0:
                                self.validGames += self.settings['likeValue']
                            elif game['like'] == 0:
                                self.validGames += self.settings['normalValue']
                            elif not self.settings['excludeDislikes']:
                                self.validGames += self.settings['dislikeValue']
                        else:
                            self.validGames += settingGate(self.settings['excludeDislikes'], game['like'] >= 0)
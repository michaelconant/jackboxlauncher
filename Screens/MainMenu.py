#This is the main menu where you can view all the games

from tkinter import * 

import os                           #Used to test if a file path is an exe

from Classes.PictureButton import *
from Classes.CanvasPicture import *

class MainMenu:
    def __init__(self, master):
        
        self.frame = Frame(master)

        #Frames

        self.topFrame = Frame(self.frame)
        self.topFrame.pack(side=TOP)

        self.leftFrame = Frame(self.frame)
        self.leftFrame.pack(side=LEFT)

        self.rightFrame = Frame(self.frame)
        self.rightFrame.pack(side=RIGHT)

        #Buttons

        self.leftButton = PictureButton(self.frame, "Pictures/GUI/left_arrow.png", text="Previous Game", compound=LEFT, font=("Arial Bold", 12), border=0, 
            relx=0, rely=1.0, x=20, y=-20, anchor=SW)
        self.leftButton.place()

        self.randomButton = PictureButton(self.frame, "Pictures/GUI/random.png", text="Random Game", compound=LEFT, font=("Arial Bold", 12), border=0,
            relx=0.5, rely=1.0, x=-150, y=-20, anchor=S)
        self.randomButton.place()

        self.playButton = PictureButton(self.frame, "Pictures/GUI/play.png", text="Play Game", compound=RIGHT, font=("Arial Bold", 12), border=0,
            relx=0.5, rely=1.0, x=150, y=-20, anchor=S)
        self.playButton.place()

        self.rightButton = PictureButton(self.frame, "Pictures/GUI/right_arrow.png", text="Next Game", compound=RIGHT, font=("Arial Bold", 12), border=0,
            relx=1.0, rely=1.0, x=-20, y=-20, anchor=SE)
        self.rightButton.place()

        self.settingsButton = PictureButton(self.frame, "Pictures/GUI/settings.png", text="Settings", compound=RIGHT, font=("Arial Bold", 12), border=0,
            relx=1.0, rely=0, x=-20, y=20, anchor=NE)
        self.settingsButton.place()

        #Labels

        self.gameLabels = []

        self.titleLabel = Label(self.topFrame, font=("Arial Bold", 32))      #Pack Name
        self.titleLabel.pack(anchor=W, side=TOP, padx=30, pady=10)

        #RightFrame

        self.gameImage = CanvasPicture(self.rightFrame, '') #Canvas for the game picture
        self.gameImage.canvas.grid(row=0,column=0,columnspan=4,padx=30)

        self.likeLabel = Label(self.rightFrame, font=("Arial Bold", 14), text="Like")
        self.likeLabel.grid(row=1,column=0,sticky=SE)
        self.likeButton = PictureButton(self.rightFrame, "Pictures/GUI/like_no.png", subsample=3)
        self.likeButton.button.grid(row=1,column=1,sticky=SW)

        self.dislikeLabel = Label(self.rightFrame, font=("Arial Bold", 14), text="Dislike")
        self.dislikeLabel.grid(row=2,column=0,sticky=NE)
        self.dislikeButton = PictureButton(self.rightFrame, "Pictures/GUI/dislike_no.png", subsample=3)
        self.dislikeButton.button.grid(row=2,column=1,sticky=NW)

        self.playersLabel = Label(self.rightFrame, font=("Arial Bold", 16, 'underline'))
        self.playersLabel.grid(row=1,column=2,sticky=E)

        self.descriptionLabel = Label(self.rightFrame, anchor=N, font=("Arial Bold", 12), height=8, width=50, wraplength=420, justify=LEFT)
        self.descriptionLabel.grid(row=2,rowspan=2,column=2,columnspan=2)

    def is_exe(self, fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    def updateButtonStates(self, packs):
        if len(packs.enabledIndexs) > 1:
            self.leftButton.button.config(state="normal")
            self.rightButton.button.config(state="normal")
        else:
            self.leftButton.button.config(state="disable")
            self.rightButton.button.config(state="disable")

        packs.updateValidGames()
        if packs.validGames > 1:
            self.randomButton.button.config(state="normal")
        else:
            self.randomButton.button.config(state="disable")

    def updatePlayButtonState(self, packs):
        if self.is_exe(packs.data[packs.currentPack]['gamePath']):
            self.playButton.button.config(state="normal")
        else:
            self.playButton.button.config(state="disable")

    def updateLikeButtons(self, packs):
        if packs.data[packs.currentPack]['games'][packs.currentGame]['like'] < 0:
            self.likeButton.changePicture("Pictures/GUI/like_no.png")
            self.dislikeButton.changePicture("Pictures/GUI/dislike_yes.png")
        elif packs.data[packs.currentPack]['games'][packs.currentGame]['like'] == 0:
            self.likeButton.changePicture("Pictures/GUI/like_no.png")
            self.dislikeButton.changePicture("Pictures/GUI/dislike_no.png")
        else:
            self.likeButton.changePicture("Pictures/GUI/like_yes.png")
            self.dislikeButton.changePicture("Pictures/GUI/dislike_no.png")

    def display(self, packs):
        self.frame.pack(fill="both", expand=True)

        if not packs.data[packs.currentPack]['enabled'] and len(packs.enabledIndexs):
            self.shiftPack(packs, 1)

        self.updateButtonStates(packs)
        self.updatePlayButtonState(packs)
        self.updateLikeButtons(packs)

    def forget(self):
        self.frame.pack_forget()

    #updates the widget colors using the current color settings
    def updateColors(self, packs):
        if packs.settings['defaultThemeEnabled']:
            bg_color = packs.defaultTheme['bg_color']
            text_color = packs.defaultTheme['text_color']
            description_color = packs.defaultTheme['description_color']
            highlight_color = packs.defaultTheme['highlight_color']
            title_color = packs.defaultTheme['title_color']
            button_text_color = packs.defaultTheme['button_text_color']
        else:
            bg_color = packs.data[packs.currentPack]['bg_color']
            text_color = packs.data[packs.currentPack]['text_color']
            description_color = packs.data[packs.currentPack]['description_color']
            highlight_color = packs.data[packs.currentPack]['highlight_color']
            title_color = packs.data[packs.currentPack]['title_color']
            button_text_color = packs.data[packs.currentPack]['button_text_color']

        self.leftButton.button['fg'] = button_text_color
        self.randomButton.button['fg'] = button_text_color
        self.playButton.button['fg'] = button_text_color
        self.rightButton.button['fg'] = button_text_color
        self.settingsButton.button['fg'] = button_text_color
        self.dislikeLabel['fg'] = button_text_color
        self.likeLabel['fg'] = button_text_color

        self.frame['bg'] = bg_color

        self.topFrame['bg'] = bg_color
        self.leftFrame['bg'] = bg_color
        self.rightFrame['bg'] = bg_color

        self.titleLabel['bg'] = bg_color
        self.titleLabel['fg'] = title_color

        self.leftButton.button['bg'] = bg_color
        self.randomButton.button['bg'] = bg_color
        self.playButton.button['bg'] = bg_color
        self.rightButton.button['bg'] = bg_color
        self.settingsButton.button['bg'] = bg_color

        self.gameImage.canvas['bg'] = bg_color
        self.dislikeLabel['bg'] = bg_color
        self.dislikeButton.button['bg'] = bg_color
        self.likeLabel['bg'] = bg_color
        self.likeButton.button['bg'] = bg_color
        self.playersLabel['bg'] = bg_color
        self.descriptionLabel['bg'] = bg_color

        self.playersLabel['fg'] = description_color
        self.descriptionLabel['fg'] = description_color

        for i in range(len(self.gameLabels)):
            self.gameLabels[i]['bg'] = bg_color
            if i != packs.currentGame:
                self.gameLabels[i]['fg'] = text_color
            else:
                self.gameLabels[i]['fg'] = highlight_color

    #change to a specific game using the index
    def changeGame(self, packs, gamePos):
        if self.gameLabels and gamePos >= 0 and gamePos < len(packs.data[packs.currentPack]['games']):

            if packs.settings['defaultThemeEnabled']:
                text_color = packs.defaultTheme['text_color']
                highlight_color = packs.defaultTheme['highlight_color']
            else:
                text_color = packs.data[packs.currentPack]['text_color']
                highlight_color = packs.data[packs.currentPack]['highlight_color']

            self.gameLabels[packs.currentGame]['fg'] = text_color
            self.gameLabels[gamePos]['fg'] = highlight_color

            self.playersLabel.config(text=str(packs.data[packs.currentPack]['games'][gamePos]['playerMin']) + ' - ' + str(packs.data[packs.currentPack]['games'][gamePos]['playerMax']) + ' Players')
            self.descriptionLabel.config(text=packs.data[packs.currentPack]['games'][gamePos]['description'])

            self.gameImage.setImage(packs.data[packs.currentPack]['picturesPath'] + packs.data[packs.currentPack]['games'][gamePos]['pictureName'])

            packs.currentGame = gamePos

            self.updateLikeButtons(packs)
        else:
            print("ERROR Index out of range - MainMenu.changeGame")

    #change to a specific pack using the index
    def changePack(self, packs, packPos):
        if packPos >= 0 and packPos < len(packs.data):

            #tempPos = 0 if packs.currentPack > len(packs.data[packPos]['games']) else packs.currentPack
            tempGamePos = (packs.currentGame, 0)[packs.currentGame >= len(packs.data[packPos]['games'])]

            self.titleLabel.config(text=packs.data[packPos]['name'])

            self.gameImage.setImage(packs.data[packPos]['picturesPath'] + packs.data[packPos]['games'][tempGamePos]['pictureName'])

            self.playersLabel.config(text=str(packs.data[packPos]['games'][tempGamePos]['playerMin']) + ' - ' + str(packs.data[packPos]['games'][tempGamePos]['playerMax']) + ' Players')
            self.descriptionLabel.config(text=packs.data[packPos]['games'][tempGamePos]['description'])

            for i in self.gameLabels:
                i.destroy()
            self.gameLabels.clear()

            for i in range(len(packs.data[packPos]['games'])):
                #Append Label to gameLabels array
                self.gameLabels.append(Label(self.leftFrame, text=packs.data[packPos]['games'][i]['name'], font=("Arial Bold", 26)))

                self.gameLabels[i].pack(anchor=W, side=TOP, padx=30, pady=20)

            packs.currentGame = tempGamePos
            packs.currentPack = packPos

            self.updatePlayButtonState(packs)
            self.updateLikeButtons(packs)

            #----- Colors -----
            self.updateColors(packs)

        else:
            print("ERROR Index out of range - MainMenu.changePack")

    #shift to a pack before or after the current pack using the offset value
    def shiftPack(self, packs, offset):

        try:
            tempPos = (packs.enabledIndexs.index(packs.currentPack) + offset) % len(packs.enabledIndexs)
            self.changePack(packs, packs.enabledIndexs[tempPos])
        except:
            tempPos = packs.currentPack
            foundFlag = False
            while not foundFlag:
                tempPos = (tempPos + offset) % len(packs.data)
                if packs.data[tempPos]['enabled']:
                    foundFlag = True
            self.changePack(packs, tempPos)
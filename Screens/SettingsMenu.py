#This is the settings menu

from tkinter import *
from tkinter import filedialog  #for files

from Classes.PictureButton import *

class SettingsMenu:
    def __init__(self, master, packs):

        bg_color = '#121212'

        #Temporary Values
        #   -Values used for settings, these are used so settings only change when the save button is pressed

        self.defaultThemeFlag = BooleanVar()
        self.defaultThemeFlag.set(packs.settings['defaultThemeEnabled'])

        self.tempPlayers = packs.settings['currentPlayers']

        self.weightLikes = BooleanVar()
        self.weightLikes.set(packs.settings['likeWeight'])
        self.excludeDislikes = BooleanVar()
        self.excludeDislikes.set(packs.settings['excludeDislikes'])

        #self.checkButtonState = [BooleanVar() for i in range(len(packs.data))]
        self.checkButtonState = []
        for i in range(len(packs.data)):
            self.checkButtonState.append(BooleanVar())
            self.checkButtonState[i].set(packs.data[i]['enabled'])

        #Master Frame

        self.frame = Frame(master)
        self.frame['bg'] = bg_color

        #Frames

        self.topFrame = Frame(self.frame)
        self.topFrame['bg'] = bg_color
        self.topFrame.pack(side=TOP)

        self.leftFrame = Frame(self.frame)
        self.leftFrame['bg'] = bg_color
        self.leftFrame.pack(side=LEFT, padx=20)

        self.rightFrame = Frame(self.frame)
        self.rightFrame['bg'] = bg_color
        self.rightFrame.pack(side=RIGHT, padx=20)

        #--- Master Frame Widgets ---

        self.homeButton = PictureButton(self.frame, "Pictures/GUI/home.png", fg='white', bg='#666666', text="Home", compound=RIGHT, font=(packs.FONTNAME, 12), border=1,
            relx=1.0, rely=0, x=-20, y=20, anchor=NE)
        self.homeButton.button.place(relx=1.0, rely=0, x=-20, y=20, anchor=NE)

        self.saveButton = PictureButton(self.frame, "Pictures/GUI/save.png", fg='white', bg='#666666', text="Save      ", compound=RIGHT, font=(packs.FONTNAME, 12), border=1,
            relx=1.0, rely=1.0, x=-20, y=-20, anchor=SE)
        self.saveButton.button.place(relx=1.0, rely=1.0, x=-20, y=-20, anchor=SE)

        #--- Top Frame Widgets ---

        Label(self.topFrame, font=(packs.FONTNAME, 32), fg='white', bg=bg_color, text='Settings').pack(side=TOP, padx=30, pady=10)

        #--- Left Frame Widgets ---

        Label(self.leftFrame, text="PACK NAME", font=(packs.FONTNAME, 16, "italic underline"), bg=bg_color, fg="white").grid(row=0,column=0,pady=10,sticky=W)
        Label(self.leftFrame, text="PACK PATH", font=(packs.FONTNAME, 16, "italic underline"), bg=bg_color, fg="white").grid(row=0,column=1,pady=10,sticky=W)

        #Loops the for how many packs there are
        self.textEntrys = []
        for i in range(len(packs.data)):
            
            #Adds a check button for the pack on the screen
            tempCheckButton = Checkbutton(self.leftFrame, variable=self.checkButtonState[i], text=packs.data[i]['name'], compound=LEFT, anchor=W, font=(packs.FONTNAME, 16), bg=bg_color, fg="white", selectcolor="black")

            #Puts Checkbutton on the grid
            tempCheckButton.grid(row=i+1,column=0,sticky=W,pady=5)

            self.textEntrys.append(Entry(self.leftFrame, width=100))                            #Creates an Entry box for the file path
            self.textEntrys[i].insert(0, packs.data[i]['gamePath'])                             #Inserts the gamePath from the pack into the Entry box
            self.textEntrys[i].grid(row=i+1,column=1,sticky=E,ipadx=0,ipady=0,padx=10,pady=5)   #Puts Entry box on the grid
            
            tempVar = Button(self.leftFrame, text=" . . . ")                                    #Creates a Button to open a file explorer to get file path
            tempVar.config(command= lambda num=i+1: self.fileButtonClicked(num))                #Assigns function to the buttion
            tempVar.grid(row=i+1,column=2,sticky=W,ipadx=0,ipady=0,padx=0,pady=5)               #Puts button onto the grid

        #--- Right Frame Widgets ---

        #Theme
        Label(self.rightFrame, text="Default Theme", font=(packs.FONTNAME, 16, "italic underline"), bg=bg_color, fg="white", anchor=W).grid(
            row=0,column=0,columnspan=3,pady=10,sticky=W)
        Checkbutton(self.rightFrame, variable=self.defaultThemeFlag, compound=TOP, bg=bg_color, fg="white", selectcolor="black").grid(
            row=1,column=0,columnspan=3,pady=2,sticky=W)
        
        #Players
        Label(self.rightFrame, text="Players", font=(packs.FONTNAME, 16, "italic underline"), bg=bg_color, fg="white", anchor=W).grid(
            row=2,column=0,columnspan=3,pady=10,sticky=W)
        
        self.minusPlayersButton = PictureButton(self.rightFrame, "Pictures/GUI/minus.png", subsample=4, bg=bg_color, compound=RIGHT, font=(packs.FONTNAME, 12))
        self.minusPlayersButton.button.grid(row=3,column=0,sticky=E)
        
        self.playersLabel = Label(self.rightFrame, font=(packs.FONTNAME, 16), bg=bg_color, fg="white", width=4)
        if packs.settings['currentPlayers'] <= 0:
            self.playersLabel.config(text="N/A")
        if packs.settings['currentPlayers'] > 16:
            self.playersLabel.config(text="17+")
        else:
            self.playersLabel.config(text=packs.settings['currentPlayers'])
        self.playersLabel.grid(row=3,column=1)
        
        self.plusPlayersButton = PictureButton(self.rightFrame, "Pictures/GUI/plus.png", subsample=4, bg=bg_color, compound=RIGHT, font=(packs.FONTNAME, 12))
        self.plusPlayersButton.button.grid(row=3,column=2,sticky=W)

        #Weighted Random
        Label(self.rightFrame, text="Like/Dislike Settings", font=(packs.FONTNAME, 16, "italic underline"), bg=bg_color, fg="white", anchor=W).grid(
            row=4,column=0,columnspan=3,pady=10,sticky=W)
        Checkbutton(self.rightFrame, variable=self.weightLikes, text="Like Status Effects Random", font=(packs.FONTNAME, 12), compound=TOP, bg=bg_color, fg="white", selectcolor="black").grid(
            row=5,column=0,columnspan=3,pady=2,sticky=W)
        Checkbutton(self.rightFrame, variable=self.excludeDislikes, text="Random Excludes Dislikes", font=(packs.FONTNAME, 12), compound=TOP, bg=bg_color, fg="white", selectcolor="black").grid(
            row=6,column=0,columnspan=3,pady=2,sticky=W)

    def fileButtonClicked(self, num):
        gameName = self.leftFrame.grid_slaves(row=num, column=0)[0]['text']

        #Opens the file explorer for the user to select their exe for the game.
        file_path = filedialog.askopenfilename(title="Select exe for " + gameName, multiple=False, filetypes=[("EXE File",".exe")])

        #if the they actually select a file it is put into the Entry box for that game
        if str(file_path):
            self.leftFrame.grid_slaves(row=num, column=1)[0].delete(0, END)
            self.leftFrame.grid_slaves(row=num, column=1)[0].insert(0, str(file_path))

    def updatePlayers(self):
        if self.tempPlayers == 0:
            self.playersLabel.config(text='N/A')
            self.minusPlayersButton.button.config(state="disable")
        elif self.tempPlayers > 16:
            self.playersLabel.config(text='17+')
            self.plusPlayersButton.button.config(state="disable")
        else:
            self.playersLabel.config(text=self.tempPlayers)
            self.minusPlayersButton.button.config(state="normal")
            self.plusPlayersButton.button.config(state="normal")

    def display(self, packs):

        for i in range(len(packs.data)):
            self.checkButtonState[i].set(packs.data[i]['enabled'])
            self.textEntrys[i].delete(0, END)
            self.textEntrys[i].insert(0, packs.data[i]['gamePath'])

        self.defaultThemeFlag.set(packs.settings['defaultThemeEnabled'])

        self.tempPlayers = packs.settings['currentPlayers']
        self.updatePlayers()

        self.weightLikes.set(packs.settings['likeWeight'])
        self.excludeDislikes.set(packs.settings['excludeDislikes'])

        self.frame.pack(fill="both", expand=True)

    def forget(self):
        self.frame.pack_forget()
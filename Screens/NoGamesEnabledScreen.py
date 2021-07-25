#this screen appears when the user disables all the packs

from tkinter import * 
from Classes.PictureButton import *

class NoGamesEnabledScreen:
    def __init__(self, master):
        
        #deep sky blue
        #sky blue
        #light blue

        bg_color = 'sky blue'

        #frames
        self.frame = Frame(master)

        self.frame['bg'] = bg_color

        #Labels
        self.titleLabel = Label(self.frame, padx=50, bg=bg_color, fg='white', font=("Arial Bold", 160), text=':(')
        self.titleLabel.pack(side=LEFT)

        self.titleLabel = Label(self.frame, padx=300, bg=bg_color, fg='white', font=("Arial Bold", 24), justify=LEFT)
        self.titleLabel.config(text='You Don\'t Have Any Packs Enabled:\n    You must enable at least one pack in the settings.')
        self.titleLabel.pack(side=LEFT)

        #Buttons
        self.settingsButton = PictureButton(self.frame, "Pictures/GUI/settings.png", text="Settings", compound=RIGHT, font=("Arial Bold", 12), border=0,
            relx=1.0, rely=0, x=-20, y=20, anchor=NE)
        self.settingsButton.button.config(bg='light blue', fg='black', border=2)
        self.settingsButton.place()

    def display(self):
        self.frame.pack(fill="both", expand=True)

    def forget(self):
        self.frame.pack_forget()
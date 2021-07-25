#This screen displays when there was an error with the json files

from tkinter import * 

class JsonErrorScreen:
    def __init__(self, master):
        
        bg_color = 'sky blue'

        self.frame = Frame(master)

        self.frame['bg'] = bg_color

        self.titleLabel = Label(self.frame, padx=50, bg=bg_color, fg='white', font=("Arial Bold", 160), text=':(')
        self.titleLabel.pack(side=LEFT)

        self.titleLabel = Label(self.frame, padx=300, bg=bg_color, fg='white', font=("Arial Bold", 24), justify=LEFT)
        self.titleLabel.config(text='Error Reading Json File:\n    This can be caused by-\n        1. Missing File\n        2. Missing Permission To Open File\n        3. The File Was Formatted Improperly')
        self.titleLabel.pack(side=LEFT)

    def display(self):
        self.frame.pack(fill="both", expand=True)

    def forget(self):
        self.frame.pack_forget()
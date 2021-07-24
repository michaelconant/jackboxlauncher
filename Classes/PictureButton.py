from tkinter import * 

class PictureButton:
    def __init__(self, master, filePath, subsample=2, text="", compound=CENTER, font=("Arial", 12), border=0, bg='gray', fg='black', relx=0, rely=0, x=0, y=0, anchor=N):
        self.relx = relx
        self.rely = rely
        self.x = x
        self.y = y
        self.anchor = anchor
        self.subsample = subsample
        
        self.button = Button(master, bg=bg, fg=fg, text=text, compound=compound, font=font, border=border)
        try:
            self.photo = PhotoImage(file = filePath)
            self.photo = self.photo.subsample(subsample, subsample)
            self.button.config(image=self.photo)
        except:
            print("ERROR FINDING FILE - PictureButton.constructor : " + filePath)

    def setPlaceProp(self, relx=0, rely=0, x=0, y=0, anchor=N):
        self.relx = relx
        self.rely = rely
        self.x = x
        self.y = y
        self.anchor = anchor

    def place(self):
        self.button.place(relx=self.relx, rely=self.rely, x=self.x, y=self.y, anchor=self.anchor)

    def pack(self, side=TOP):
        self.button.pack(side=side)

    def changePicture(self, filePath):
        try:
            self.photo = PhotoImage(file = filePath)
            self.photo = self.photo.subsample(self.subsample, self.subsample)
            self.button.config(image=self.photo)
        except:
            print("ERROR FINDING FILE - PictureButton.constructor : " + filePath)

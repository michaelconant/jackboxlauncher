from tkinter import * 

class CanvasPicture:
    def __init__(self, master, filePath):
        try:
            self.canvas = Canvas(master, width=640, height=360, bg='cyan')
            if filePath:
                self.photo = PhotoImage(file = filePath)
                self.canvas.create_image(2, 2, anchor=NW, image=self.photo)
        except:
            print("ERROR FINDING FILE - CanvasPicture.constructor : " + filePath)

    def pack(self, side=TOP, padx=30, pady=0):
        self.canvas.pack(side=side, padx=padx, pady=pady)

    def delete_all(self):
        self.canvas.delete("all")

    def setImage(self, filePath):
        try:
            self.photo = PhotoImage(file = filePath)
            self.canvas.create_image(2, 2, anchor=NW, image=self.photo)
        except:
            print("ERROR FINDING FILE - CanvasPicture.setImage : " + filePath)

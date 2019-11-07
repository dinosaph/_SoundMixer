import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import tkinter
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from pygame import mixer

EDIT_MODE = False
CURRENT_BTN = 1
SOUNDS = {1: [0, 0], 2: [0, 0], 3: [0, 0], 4: [0, 0], 5: [0, 0], 6: [0, 0], 7: [0, 0], 8: [0, 0], 9: [0, 0]}

class Fr(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

        mixer.init(44100)

        playImage = Image.open("play.png")
        playImage = playImage.resize((100, 100), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(playImage)
        self.BUTTONS = []

        self.btnColor = "white"
        self.btnText = "white"
        self.bt0 = Button(self, text="EDIT", bg="green", fg="white")
        self.bt0.grid(row=0, columnspan=3, sticky=NSEW)
        self.bt1 = Button(self, image=self.render, compound=tkinter.CENTER, bg=self.btnColor, fg=self.btnText)
        self.bt1.grid(row=1)
        self.bt2 = Button(self, image=self.render, compound=tkinter.CENTER, bg=self.btnColor, fg=self.btnText)
        self.bt2.grid(row=1, column=1)
        self.bt3 = Button(self, image=self.render, compound=tkinter.CENTER, bg=self.btnColor, fg=self.btnText)
        self.bt3.grid(row=1, column=2)
        self.bt4 = Button(self, image=self.render, compound=tkinter.CENTER, bg=self.btnColor, fg=self.btnText)
        self.bt4.grid(row=2)
        self.bt5 = Button(self, image=self.render, compound=tkinter.CENTER, bg=self.btnColor, fg=self.btnText)
        self.bt5.grid(row=2, column=1)
        self.bt6 = Button(self, image=self.render, compound=tkinter.CENTER, bg=self.btnColor, fg=self.btnText)
        self.bt6.grid(row=2, column=2)
        self.bt7 = Button(self, image=self.render, compound=tkinter.CENTER, bg=self.btnColor, fg=self.btnText)
        self.bt7.grid(row=3)
        self.bt8 = Button(self, image=self.render, compound=tkinter.CENTER, bg=self.btnColor, fg=self.btnText)
        self.bt8.grid(row=3, column=1)
        self.bt9 = Button(self, image=self.render, compound=tkinter.CENTER, bg=self.btnColor, fg=self.btnText)
        self.bt9.grid(row=3, column=2)
        self.BUTTONS.extend([self.bt1, self.bt2, self.bt3, self.bt4, self.bt5, self.bt6, self.bt7, self.bt8, self.bt9])

        self.bt0.bind("<ButtonPress>", self.editClick)
        self.bt1.bind("<ButtonPress>", self.onClick)
        self.bt2.bind("<ButtonPress>", self.onClick)
        self.bt3.bind("<ButtonPress>", self.onClick)
        self.bt4.bind("<ButtonPress>", self.onClick)
        self.bt5.bind("<ButtonPress>", self.onClick)
        self.bt6.bind("<ButtonPress>", self.onClick)
        self.bt7.bind("<ButtonPress>", self.onClick)
        self.bt8.bind("<ButtonPress>", self.onClick)
        self.bt9.bind("<ButtonPress>", self.onClick)

    def refreshColors(self):
        global SOUNDS, EDIT_MODE
        if EDIT_MODE:
            self.bt0.config(bg="pink", fg="black", text="DONE")
        else:
            self.bt0.config(bg="green", fg="white", text="EDIT")

        for i in range(1, len(SOUNDS) + 1):
            if SOUNDS[i][0] == 0:
                if EDIT_MODE:
                    self.BUTTONS[i - 1].config(bg="red")
                else:
                    self.BUTTONS[i - 1].config(bg="white")
            else:
                self.BUTTONS[i - 1].config(bg="green", text=SOUNDS[i][0][-15:-4])

    def editClick(self, event):
        global EDIT_MODE
        if EDIT_MODE:
            EDIT_MODE = False
        else:
            EDIT_MODE = True
        self.refreshColors()

    def doneEditting(self):
        global EDIT_MODE
        EDIT_MODE = False
        self.refreshColors()

    def onClick(self, event):
        btn = str(event.widget)
        if btn.endswith('2'):
            self.playSound(1)
        elif btn.endswith('3'):
            self.playSound(2)
        elif btn.endswith('4'):
            self.playSound(3)
        elif btn.endswith('5'):
            self.playSound(4)
        elif btn.endswith('6'):
            self.playSound(5)
        elif btn.endswith('7'):
            self.playSound(6)
        elif btn.endswith('8'):
            self.playSound(7)
        elif btn.endswith('9'):
            self.playSound(8)
        elif btn.endswith('0'):
            self.playSound(9)

    def playSound(self, btn):
        global SOUNDS, EDIT_MODE
        if EDIT_MODE:
            self.loadSound(btn)
        else:
            if SOUNDS[btn][0] != 0:
                SOUNDS[btn][1].play()
            else:
                self.loadSound(btn)

    def loadSound(self, btn):
        global EDIT_MODE, SOUNDS
        filename = filedialog.askopenfilename(initialdir = ".",title = "Select file",filetypes = (("wav files","*.wav"),("all files","*.*")))
        SOUNDS[btn][0] = filename
        SOUNDS[btn][1] = mixer.Sound(SOUNDS[btn][0])
        self.refreshColors()
        if not EDIT_MODE:
            self.playSound(btn)
    
if __name__ == "__main__":
    root = Tk()
    root.title("Soundmixer")
    Fr(root).pack()
    root.mainloop()
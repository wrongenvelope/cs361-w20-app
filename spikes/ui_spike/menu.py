import tkinter as tk
import sys
from functools import partial
from style import *

class AppMenuBar(tk.Menu):
    def __init__(self, parent, themes):
        tk.Menu.__init__(self, parent)

        # File Menu
        fileMenu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="File",underline=0, menu=fileMenu)
        fileMenu.add_command(label="Export To Do List", underline=1, command=self.exportToDo)
        fileMenu.add_command(label="Export Appointments", underline=1, command=self.exportAppts)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", underline=1, command=self.quit, accelerator="Ctrl+Q")

        self.bind_all("<Control-q>", self.quit)
        
        # Theme Menu (roll into settings menu eventually?)
        themeMenu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="Theme",underline=0, menu=themeMenu)

        ## set theme 1
        themeMenu.add_command(label="Dracula", underline=1, command=partial(self.setDraculaTheme, parent, themes))

        ## set theme 2
        themeMenu.add_command(label="Mint Chocolate Chip", underline=1, command=partial(self.setMintTheme, parent, themes))


        # Help Menu
        helpMenu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="Help",underline=0, menu=helpMenu)
        helpMenu.add_command(label="About", underline=1, command=self.aboutUs)
        
    def exportToDo(self):
        sys.exit(0)

    def exportAppts(self):
        sys.exit(0)
        
    def quit(self, event=None):
        sys.exit(0)

    def setDraculaTheme(self, parent, themes):
        parent.config(background='#282A36')
        themes.theme_use('dracula')

    def setMintTheme(self, parent, themes):
        parent.config(background='#FFFFFF')
        themes.theme_use('mintChocolateChip')
        
    def aboutUs(self):
        sys.exit(0)

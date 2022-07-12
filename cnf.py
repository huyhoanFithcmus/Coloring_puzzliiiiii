import tkinter 
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import pysat
import os 
from os import system
import filecmp

class GUI:
    def close(self):
        self.root.destroy()
        self.root.quit()
        os._exit(0)

    def __init__(self):
        self.root = Tk()
        self.root.title("Coloring Puzzle")
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.root.configure(background='burlywood1')
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)

        self.lbframe = LabelFrame(self.root, text='Algorithm', font='Times 16')
        self.Algorithm = ttk.Combobox(self.root, values=['Astar', 'Backtracking', 'Brute force', 'PySAT'])
        self.butBrowser = Button(
            self.root, text='Browse Files', font='Times 12', command=lambda: self.browseFiles())
        self.butStart = Button(
            self.root, text='Start', font='Times 12', command=lambda: self.start())
        self.LbinfoFrame = LabelFrame(self.root, bg='burlywood1')
        self.lbframe.grid(row=4, columnspan=2)
        self.Algorithm.grid(row=2, column=0, sticky=W, padx=8)
        self.butBrowser.grid(row=0, column=1)
        self.butStart.grid(row=1, column=1)
        self.LbinfoFrame.grid(row=3, columnspan=2)
        self.root.mainloop()

    def browseFiles(self):
        filename = filedialog.askopenfilename(
            title="Select a File",
            filetypes=[("Text File", "*.txt")])
        self.entAddr.delete(0, END)
        self.entAddr.insert(0, filename)
    
    def start(self):
        self.halt = False
        self.stepHeur = Label(self.root, font='Times 12')
        self.entAddr = Text(self.root, font='Times 12', height=1)
        self.Delay = ttk.Combobox(self.root, values=['0.5', '0.75', '1.0', '1.25', '1.5'])
        self.lbframe = LabelFrame(self.root, text='Algorithm', font='Times 16')
        self.Algorithm = ttk.Combobox(self.root, values=['Astar', 'Backtracking', 'Brute force', 'PySAT'])
        self.butBrowser = Button(
            self.root, text='Browse Files', font='Times 12', command=lambda: self.browseFiles())
        self.butStart = Button(
            self.root, text='Start', font='Times 12', command=lambda: self.start())
        self.LbinfoFrame = LabelFrame(self.root, bg='burlywood1')
        self.gridGUI()
        self.root.mainloop()

    def gridGUI(self):
        self.lbframe.grid(row=4, columnspan=2)
        self.Algorithm.grid(row=2, column=0, sticky=W, padx=8)
        self.butBrowser.grid(row=0, column=1)
        self.butStart.grid(row=1, column=1)
        self.LbinfoFrame.grid(row=3, columnspan=2)
        self.stepHeur.grid(row=0, column=0)
        self.entAddr.grid(row=1, column=0)
        self.Delay.grid(row=2, column=0)
        self.root.mainloop()


class CNF:
    pass

# main function
if __name__ == '__main__':
    # run GUI
    GUI()
    # run CNF
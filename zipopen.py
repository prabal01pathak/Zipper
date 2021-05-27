from tkinter import filedialog
from tkinter import *
import tkinter as tk

class Application(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master= master 
        self.pack()
        self.creat_widgets()

    def creat_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there['text']='SELECT'
        self.hi_there['command']= self.open_zip
        self.hi_there.pack(side='top')
        self.quit = tk.Button(self,text = 'QUIT',fg = 'red',command = self.master.destroy)
        self.quit.pack(side='bottom')
    def open_zip(self):
        self.fill = tk.Label(root,text = f'File Name --> {self.files}\n',fg = 'green',bg = 'white')
        self.fill.pack(side = 'left')
        fileName.set(self.files)
        self.fill = tk.Label(root,textvariable = fileName)
        print(self.fill)
                count = 0
                print(l)
                for i in range(len(l:
                    print(i)
                    self.label = Label(root,text = f'Files are {l[count].filename}\n',fg = 'blue',bg = 'white')
                self.label.pack(side = 'left')
                count +=1
    app = Application(master = root)
    app.mainloop()  


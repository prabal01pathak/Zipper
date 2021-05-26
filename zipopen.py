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
        self.files =filedialog.askopenfilenames()
        fileName = StringVar()
        self.name = tk.Entry(root,width = 8,textvariable=self.files)
        self.fill = tk.Label(root,textvariable = self.files)
        self.name.pack(side = 'top')
        print(self.files)

if __name__ == "__main__":
    root = tk.Tk()
    root.columnconfigure(0,weight=1)
    root.rowconfigure(0,weight=1)
    root.title('ZIPPER')
    app = Application(master = root)
    app.mainloop()  


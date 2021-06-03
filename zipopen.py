from functools import partial
from zipfile import ZipFile
from tkinter import filedialog
from tkinter import *
import tkinter as tk
import time
import os
import sys
from datetime import datetime

#This is main class for handling frame and widgets.

class Application(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master= master 
        self.pack()
        self.creat_widgets()

#widgets for selecting file and processing .
    def creat_widgets(self):
        self.ask_file = tk.Button(self,text = 'SELECT',fg = 'blue',command = self.ask_zip) # Ask for zip file.
        self.ask_file.pack()
        self.quit = tk.Button(self,text = 'QUIT',fg = 'red',command = self.master.destroy) #exit from application.
        self.quit.pack()

    #For selecting zip file.

    def ask_zip(self):
        files = filedialog.askopenfilename(filetypes =[('zip {.zip}')]) #dialog only zip files.
        data = StringVar()
        data.set(files) #fill data with name of file.
        entry = Entry(root,textvariable = data) #Name of file.
        entry.place(x=10,y=30)
        show = Button(root,text = 'SHOW',command = partial(self.open_zip,data.get())) #show list files in archive.
        show.place(x = 150,y=25)
        for_extract = Button(text = 'EXTRACT ALL',command = partial(self.extract_all,files)) #Extract all member of archive.
        for_extract.place(x =200,y = 25)

    #This method will open zip file and give information about file.

    def open_zip(self,files):
        with ZipFile(files,'r') as zips:
            l = zips.infolist()
            for i in range(len(l)):
                count = Label(text = f'{i+1}.') 
                count.place(x = 1,y=i*30+60)
                info_data = StringVar()
                info_data.set(l[i].filename)
                label = Entry(root,textvariable =info_data,fg = 'blue',bg = 'white') #To show Name of files in archive.
                label.place(x=15,y=i*30+60)

    #For extracting all files from archive.
    def extract_all(self,files):
        with ZipFile(files,'r') as zips:
            ask_folder = filedialog.askdirectory()
            extract_path = str(ask_folder)
            zips.extractall(path=extract_path)
            time.sleep(1)
            label_done = Label(root , text = 'Done' )
            label_done.place(x = 150 , y = 90)
            os.startfile(ask_folder) # prompt with extracted files.

if __name__ == "__main__":
    root = Tk()
    root.geometry('200x200')
    app = Application(master = root)
    root.mainloop()  


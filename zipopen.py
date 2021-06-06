from functools import partial
from zipfile import ZipFile
from tkinter import filedialog
from tkinter import *
from tkinter import ttk
import tkinter as tk
import time
import os
import sys
from datetime import datetime
import shutil
from tarfile import TarFile
from pathlib import Path 
import glob

#This is main class for handling frame and widgets.

class Application(ttk.Frame):
    def __init__(self):
        super().__init__()
        self.pack()
        self.creat_widgets()
        

#widgets for selecting file and processing .
    def creat_widgets(self):
        self.make_archive = Button(self,text = 'MAKE',fg ='pink',command = self.make_archive)
        self.make_archive.pack(side = LEFT,expand = False)
        self.for_tar = Button(self,text = 'TAR',fg = 'green',command = self.ask_tarfile)
        self.for_tar.pack(side = LEFT , expand = False)
        self.ask_file = tk.Button(self,text = 'ZIP',fg = 'blue',command = self.ask_zip) # Ask for zip file.
        self.ask_file.pack(side = LEFT , expand =1,padx = 5 ,pady = 4)
        self.quit = tk.Button(self,text = 'QUIT',fg = 'red',command = self.master.destroy) #exit from application.
        self.quit.pack(side = LEFT , expand = 1,padx = 5 ,pady = 4)
       # self.refresh = Button(self,text = 'Refresh' , command = refresh)
       # self.refresh.pack()
        self.show_time = Label(self,fg = 'white',bg = 'black')
        self.digital_clock()
        self.show_time.pack(fill = X,expand = 1)

    #For selecting zip file.
    def digital_clock(self):
        times = time.strftime('%H:%M')
        date = datetime.now().date()
        self.show_time.config(text =f'Date : {date} \n Time: {times}')
        self.show_time.after(200,self.digital_clock)

    def ask_zip(self):
        global lists
        lists = []
        files = filedialog.askopenfilename(filetypes =[('zip {.zip}')]) #dialog only zip files.
        if len(files) == 0:
            label = Label(root , text = "please select zipfile")
            label.pack()
            lists.append(label)
            button = Button(root ,text = 'Delete',command = self.refresh)
            button.pack()
            lists.append(button)
        else:
            data = StringVar()
            data.set(files) #fill data with name of file.
            entry = Entry(root,textvariable = data) #Name of file.
            entry.place(x=10,y=30)
            lists.append(entry)
            show = Button(root,text = 'SHOW',command = partial(self.open_zip,data.get())) #show list files in archive.
            show.place(x = 150,y=25)
            lists.append(show)
            refresh = Button(root ,text = 'RFRESH', command = self.refresh)
            refresh.pack()
            lists.append(refresh)
            for_extract = Button(text = 'EXTRACT ALL',command = partial(self.extract_all,files)) #Extract all member of archive.
            for_extract.place(x =200,y = 25)
            lists.append(for_extract)

    #This method will open zip file and give information about file.

    def open_zip(self,files):
        vscrollbar = Scrollbar(self,orient=VERTICAL)
        vscrollbar.pack(fill = Y,side =RIGHT ,expand = False)
        lists.append(vscrollbar)
        with ZipFile(files,'r') as zips:
            l = zips.infolist()
            for i in range(len(l)):
                count = Label(text = f'{i+1}.') 
                lists.append(count)
                count.place(x = 1,y=i*30+60)
                info_data = StringVar()
                info_data.set(l[i].filename)
                label_entry = Entry(root,textvariable =info_data,fg = 'blue',bg = 'white') #To show Name of files in archive.
                lists.append(label_entry)
                label_entry.place(x=15,y=i*30+60)
                

    #For extracting all files from archive.
    def extract_all(self,files):
        try:
            with ZipFile(files,'r') as zips:
                ask_folder = filedialog.askdirectory()
                label = Label(root , text = ask_folder)
                label.pack(fill = BOTH ,expand =1 ,padx = 5 ,pady = 5)
                lists.append(label)
                extract_path = str(ask_folder)
                zips.extractall(path=extract_path)
                time.sleep(1)
                label_done = Label(root , text = 'Done' )
                label_done.place(x = 150 , y = 90)
                lists.append(label_done)
                os.startfile(ask_folder) # prompt with extracted files.
        except:
            label_error = Label(root,text = 'error')
            label_error.pack()
            lists.append(label_error)

    def refresh(self):
            l =  lists
            for i in l:
                i.destroy()
    def ask_tarfile(self):
        global asked_file
        asked_file = str(filedialog.askopenfilename())
        with TarFile(asked_file,'r') as tar:
            member = tar.getmembers()
            for i in range(len(member)):
                label_member = Label(root,text = f'{i +1}. {member[i].name}')
                label_member.pack()
            extract = Button(root,text = 'Extract',command = self.open_tar)
            extract.pack()
    def open_tar(self):
        with TarFile(asked_file , 'r') as tar:
            extract_folder = filedialog.askdirectory()
            tar.extractall(path = extract_folder)
            os.startfile(extract_folder)
    def make_archive(self):
        ask_folder = str(filedialog.askdirectory())
        print(ask_folder)
        

#    self.master.destroy()
#    root = Tk()
#    Application(master = root)
#    root.mainloop()
if __name__ == "__main__":
    root = Tk()
    app = Application()
    root.mainloop()  


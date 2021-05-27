import tkinter as tk
from tkinter import *
from tkinter import filedialog
from zipfile import ZipFile
import inspect
import sys
import os
import time
import subprocess





def zip_file():

    ''' this method will 
    extract zip file'''
    directory = filedialog.askopenfilename(filetypes = [('zip {.zip}')])
    print(directory)
    try:
        with ZipFile(directory,'r') as zip:
            print(zip.printdir())
            user_op = input('Do you want to extract all or any file(all/1/n):')

            if user_op.lower() == 'all':
                zip_extract_all(zip)
            elif user_op.lower()=='1':
                zip_extract_one(zip)

            else:
                print("ok!")

    except AttributeError as e:
        print('Error: Please select zip file\n ')
        user = input('Would you like to try again(y/n): ')
        if user.lower()=='y':
            zip_file()
        else:
            print('ok')
            time.sleep(2)
            sys.exit()


#for extracting all archieve files.

def zip_extract_all(zip):
    x = inspect.stack()[0][3]
    print('Please select folder where you want to extract')
    print('look around')
    file_op = filedialog.askdirectory()
    extract_path = str(file_op)
    if os.path.exists(extract_path):
        zip.extractall(path=extract_path)
        print("done!")
        os.startfile(extract_path)
        time.sleep(5)
    else:
        user_chance(zip,x)

#for extracting single zip file.
def zip_extract_one(zip):
    x = inspect.stack()[0][3]
    member_to_extract = input('Please provide Name of member:')
    print('look around')
    extract_path = filedialog.askdirectory(title='Select Extract Folder')
    try:
        zip.extract(member=member_to_extract,path = extract_path)
        print('Done!')
        os.startfile(extract_path)
    except KeyError as e:
        print(e)
        user_chance(zip,x)


#if File not found then it will handel user.

def user_chance(zip,x):
    print('Path is invalid')
    user = input('would you like to try again(y/n): ')
    if str(x)=='zip_extract_all':
        if user.lower() == 'y':
            zip_extract_all(zip)
    elif str(x)=='zip_extract_one':
        if user.lower() == 'y':
            zip_extract_one(zip)
    print('ok')
    time.sleep(2)
    sys.exit()

class ZipWrite:
    def zip_write(self):
        directory= filedialog.askopenfilenames()
        arch_path = filedialog.asksaveasfilename(filetypes=[('zip {.zip}')])
        zip_name = str(arch_path) + '.zip'
        with ZipFile(zip_name ,'w') as zip_w:
            for name in directory:
                print(name)
                user_input = input('Would you like to reaname file(y/n): ')
                if user_input.lower()== 'y':
                    arc_name = input('Please provide name with folder name: ')
                    print(arc_name)
                    zip_w.write(name,arcname = arc_name)
                else:
                    zip_w.write(name)
            print('Done')
            time.sleep(1)
    def zip_append(self,name):
        with ZipFile(name,'a') as zip_a:
            print('Older Archive\n |-------------------------------|')
            print(zip_a.printdir())
            print(' |--------------------------| \nProvide files')
            files = filedialog.askopenfilenames()
            print(files)
            for item in files:
                print(item)
                user_input = input('Would you like to reaname file(y/n): ')
                if user_input.lower()== 'y':
                    arc_name = input('Please provide name with folder name: ')
                    print(f'{arc_name} \n |--------------------------|')
                    zip_a.write(name,arcname=arc_name) 
                    print(f'\n Done  with name --> {arc_name}')
                else:
                    zip_a.write(item)
                    print('Done without rename')

           

# This is for decleartion of file todo
def user_input():
    user_input = input('Extract or Write or Append(e/w/a): ')
    if user_input.lower() == 'e':
        zip_file()
    elif user_input.lower()=='w':
        ZipWrite().zip_write()
    elif user_input.lower()=='a':
        name = filedialog.askopenfilename(filetypes=[('zip { .zip}')])
        ZipWrite().zip_append(name)
        print('done')
    else:
        print('quit...')
        time.sleep(1)
        sys.exit()

if __name__ == "__main__":
    a = print('proceeding..')
    root = Tk()
    root.withdraw()
    user_input()

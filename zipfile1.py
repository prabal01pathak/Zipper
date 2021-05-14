from zipfile import ZipFile
import inspect
import sys
import os
import time
import subprocess

BASE_DIR = os.path.expanduser('~')



### For Extracting zip File in user defined path 

def zip_file():

    ''' this method will 
    extract zip file'''

    # Taking user input path

    user_input = input("please provide zip file Path: ")
    file_zip =  os.path.join(BASE_DIR,user_input)
    try:
        with ZipFile(file_zip,'r') as zip:
            print(zip.printdir())
            user_op = input('Do you want to extract all or any file(all/1/n):')

            if user_op.lower() == 'all':
                zip_extract_all(zip)
            elif user_op.lower()=='1':
                zip_extract_one(zip)

            else:
                print("ok!")

    except FileNotFoundError as e:
        print(e)
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
    extract_path = os.path.join(BASE_DIR,input('Provide path :'))
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
    extract_path = os.path.join(BASE_DIR,input('Provide path :'))
    if os.path.exists(extract_path):
        try:
            zip.extract(member=member_to_extract,path = extract_path)
            print('Done!')
            os.startfile(extract_path)
        except KeyError as e:
            print(e)
            user_chance(zip,x)
    else:
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
    else:
        print('ok')
        time.sleep(2)
        sys.exit()

    

### This is for decleartion of file type

if __name__ == "__main__":
    zip_file()

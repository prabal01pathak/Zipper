from zipfile import ZipFile
import sys
import os
import csv
import time

BASE_DIR = os.path.expanduser('~')

### For reading csv file 

def csv_read():

    """ This method will
    read csv file with reader
    method"""


    try:
        user_input = input("please Provide csv File path: ")
        file_dir =  os.path.join(BASE_DIR,user_input)                 #Adding with home dir.

        with open(file_dir,'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            count = 0
            print("we are reading file")

            for csv_data in csv_reader:
                if count>5:
                    break
                print(csv_data)
                count +=1

        time.sleep(6)
        sys.exit()

    except FileNotFoundError:
        print('provide right path')
        user_choose = input('Would you like to try again(y/n):')         #If user want to try again 

        if user_choose.lower() == 'y':
            csv_read()

        else:
            sys.exit()

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
                extract_path = os.path.join(BASE_DIR,input('Provide path :'))
                zip.extractall(path=extract_path)
                print("done")
                time.sleep(5)

            elif user_op.lower()=='1':
                member_to_extract = input('Please provide Name of member:')
                extract_path = os.path.join(BASE_DIR,input('Provide path :'))
                if os.path.exists(extract_path):
                    zip.extract(member=member_to_extract,path = extract_path)
                    print('Done')
                    time.sleep(5)
                else:
                    print('Path is invalid')
                    user = input('would you like to try again(y/n): ')
                    if user.lower() == 'y':
                        zip_file()
                    print('ok')
                    time.sleep(2)

            else:
                print("ok!")

    except FileNotFoundError as e:
        print(e)
        user_choose = input('would you like try again(y/n):')

        if user_choose.lower()=='y':
            zip_file()
        sys.exit()


### This is for decleartion of file type


def user_input():
    user_op = input("What type of file you want to open (zip/csv): ")
    
    #if user want to read csv file

    if user_op.lower() == "csv":
        csv_read()


    #if user want to extract zip file
    
    elif user_op.lower() == "zip":
        zip_file()

    else:
        print("please provide right option")



if __name__ == "__main__":
    user_input()

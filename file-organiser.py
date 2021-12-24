import shutil
import os

path = input("Enter the path of the file: ") # Enter the path of the file
list = os.listdir(path) # list of files in the directory

for file in list: # iterate through the list
    name, ext = os.path.splitext(file) # split the file name and extension
    ext = ext[1:] # remove the dot from the extension           
    if ext == '': # if the file is a directory
        continue # skip the directory
    if os.path.exists(path + '/' + ext): # if the directory exists
        shutil.move(path + '/' + file, path + '/' + ext + '/' + file) # move the file to the directory
    else: # if the directory does not exist
        os.makedirs(path + '/' + ext) # create the directory
        shutil.move(path + '/' + file, path + '/' + ext + '/' + file) # move the file to the directory


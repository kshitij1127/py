# write a code to remove files from a directory which are older than 30 days
import os 
import shutil
import time

path = 'C:/Users/kshitij/desktop/python-projects/randomjunkfiles'
days = 30

time.time()
seconds = time.time() - (days * 24 * 60 * 60)

everything = os.walk(path)

if os.path.exists(path):
    print('Path exists')
    list = os.listdir(path)
    for file in list:
        time.ctime = os.stat(path).st_ctime
        if time.ctime < seconds:
            print('File removed')
            os.remove(path + '/' + file)
        elif time.ctime > seconds:
            print('File is in the safe zone')

    for dirpath, dirnames, filenames in everything:
        for file in filenames:
            time.ctime = os.stat(path).st_ctime
            if time.ctime < seconds:
                print('File removed')
                os.remove(path + '/' + file)
            elif time.ctime > seconds:
                print('File is in the safe zone')

else:
    print('path does not exist')

    
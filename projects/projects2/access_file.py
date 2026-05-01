import os


directory = "c:/users/nami/Downloads/"

with os.scandir(directory) as entries:  # os.scandir() is a function that returns an iterator of os.DirEntry objects corresponding to the entries in the directory given by path.
    for entry in entries:
        print(entry.name) # entry.name is the name of the file or directory represented by the os.DirEntry object.
        
        
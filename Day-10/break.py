import os

folders = input("please provide list of folders name with spacess in between: ").split()

# print(folders)

for folder in folders:

    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("please provide valid folder name, looks like this folder does not exists: " + folder)
        break

    except PermissionError:
        print("No access to this folder " + folder)
        break

    print("==== listing files for the folder -  " + folder)
    

    for file in files:
        print(file)


# python .\break.py
# please provide list of folders name with spacess in between: xyz opt
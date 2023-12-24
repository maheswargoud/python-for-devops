import os

folders = input("please provide list of folders name with spacess in between: ").split()

# print(folders)

for folder in folders:
    files = os.listdir(folder)
    print("==== listing files for the folder -  " + folder)
    # print(files)

for file in files:
    print(file)



import sys

type = sys.argv[1]

if type == "t2.micro":
    print("it will charge you 2 dollars for a day")

elif type == "t2.medium":
    print("it will charge you 4 dollars for a day")

elif type == "t2.xlarge":
    print("it will charge you 8 dollars for a day")

elif type == "m5.xlarge":
    print("it will charge you 15 dollars for a day")

else:
    print("Please provide valid instance type")




"""

python hello.py t2.micro
python hello.py t2.medium
python hello.py t2.xlarge
python hello.py m5.xlarge
python hello.py t2.xyz

"""
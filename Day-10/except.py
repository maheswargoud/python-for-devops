# import sys

# num1 = sys.argv[1]
# num2 = sys.argv[2]

num1 = 2
num2 = 0

try:
    div = num1 / num2
    print(div)
except ZeroDivisionError:
    print("please do not enter zero " )

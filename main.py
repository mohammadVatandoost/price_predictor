# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def readData(csvfile):
    with open(csvfile, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        i = 0
        for row in reader:


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    csvfile = "./Attack-Data/"
    data = readData(csvfile)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/

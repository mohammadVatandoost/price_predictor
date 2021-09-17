# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv
from src.data.data import Data
import src.logger.logger as log
from scipy.fft import fft, ifft


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def readData(csvfile, logger):
    dataSet = []
    with open(csvfile, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        i = 0
        for row in reader:
            if i == 0:
                i = i + 1
                continue
            # element = row[0].split(",")
            if len(row) < 8 :
                logger.error("row length is not enough, len(row): %d, row = %s",
                             len(row), row )
                continue
            temp = Data(row[0], row[1], row[2], row[3], row[4], row[5],
                        row[6], row[7])
            dataSet.append(temp)

    return dataSet

def preProcessData(rawDataSet):
    X = []
    Y = []
    setSize = 5
    for i in range(len(rawDataSet)-setSize):
        temp = []
        for j in range(setSize-1):
            temp.append(rawDataSet[i+j].Low)
            temp.append(rawDataSet[i + j].High)
            temp.append(rawDataSet[i + j].Open)
            temp.append(rawDataSet[i + j].Close)
            temp.append(rawDataSet[i + j].Volume)
        X.append(temp)
        Y.append(rawDataSet[i + setSize].Close)
    return X,Y
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    log_provider = log.init()
    logger = log_provider.get_scope("main")
    csvfile = "./ETH_1H.csv"
    rawDataSet = readData(csvfile, log_provider.get_scope("read_data"))
    rawDataSet = rawDataSet[::-1]
    logger.info("dataSet length = %d", len(rawDataSet))
    logger.info("first data date = %s", rawDataSet[0].Date)
    logger.info("last data date = %s", rawDataSet[len(rawDataSet)-1].Date)
    X, Y = preProcessData(rawDataSet)
    print(X)
    print("\n ================ \n")
    print(Y)
    


    # for i in range(5, len(rawDataSet)):
        # y = fft(x)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

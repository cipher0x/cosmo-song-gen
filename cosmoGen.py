#!/usr/bin/python3

import sys
from pathlib import Path

#data = Path('sunEntropy.bin').read_bytes()
#
#for i in range(0, int(len(data)/4)):
#    start = i
#    stop = i+4
#    value = int.from_bytes(data[start:stop], byteorder='little', signed=False)
#    print(value)

class rtl_entropy_file:
    def __init__(self,fileName):
        self.fileName = fileName
        self.iter = 0
        self.__openFile__()
        self.__get_min_max_file__()


    def __openFile__(self):
        self.data = open(self.fileName.encode(), "rb").read()
        #self.data = open(str(self.fileName), "r").read()

    ###
    # @brief sets self.max, self.min, and self.maxIter from objects binary file
    # @params
    # @return
    #
    ###
    def __get_min_max_file__(self):
        min = sys.maxsize
        max = 0
        bk_iter = self.iter
        self.iter = 0
        self.maxIter = int(len(self.data)/4)
        for i in range(0, self.maxIter):
            current_word = self.popWord()
            if current_word > max:
                max = current_word
            if current_word < min:
                min = current_word
        self.iter = bk_iter
        self.max = max
        self.min = min

    ###
    # @brief gets max number from file
    # @params
    # @return max number from file
    #
    ###
    def getMaxIter(self):
        return self.maxIter

    ###
    # @brief gets max number from file
    # @params
    # @return max number from file
    #
    ###
    def getMax(self):
        return self.max
        self.maxIter = int(len(self.data)/4)

    ###
    # @brief get min number from file
    # @params
    # @return min number from file
    #
    ###
    def getMin(self):
        return self.min

    def pop(self):
        value = int.from_bytes(self.data[1:4], byteorder='little', signed=False)
        return value

    ###
    # @brief pops 4 byte postive word from binary object file, or -1 at end of list
    # @params
    # @return min number from file or -1 at EOF
    #
    ###
    def popWord(self):
        if self.iter >= self.maxIter * 4:
            return -1

        start = self.iter
        stop = self.iter + 4

        self.iter = self.iter + 4
        value = int.from_bytes((self.data[start:stop]), byteorder='little', signed=False)
        return value

    ###
    # @breif gets a random number between 0.0 and 1.0
    # @ params
    # @return float between 0.0 and 1.0, -1.0 on error
    ###
    def random(self):
        number = self.popWord()
        if number == -1:
            return number
        diff = self.max - self.min
        randNum = number / diff
        return randNum


###
# @brief entrypoint
# @return status code
###
def main():
    fname = "sunEntropy.bin"
    entropy = rtl_entropy_file(fname)
    print(entropy.getMax())
    print(entropy.getMin())
    print(entropy.getMaxIter())

    numberCount = 0
    while True:
        number = entropy.random()
        if number == -1:
            break;
        numberCount = numberCount+1
        print (number)
    print(numberCount)

    #print(entropy)
    print("end")

main()

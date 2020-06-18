import sys

def testList(value):
    print(isListOfInts(value))

def isListOfInts(list):

    try:
        if(type(list).__name__ == "tuple"):
            returnValue = ""
            raise TypeError("arg not of <list> type")

        elif(type(list).__name__ == "list"):
            if(len(list) == 0):
                returnValue = True
            for i in range(len(list)):
                if(type(list[i]).__name__ == "int"):
                    returnValue = True
                else:
                    returnValue = False
                    sys.exit(0)
    expect ValueError as te:
        print("arg not of <list> type")
    expect TypeError as te:
        print("arg not of <list> type").
    finally:
        if(returnValue!=""):
            return returnValue
        else:
            return ""
if __name__ == "__main__":
    inputs = [[], [1], [1, 2] [0], ['1'], [1, 'a'], ['a', 1], [1, 1.],[1., 1.], (1, 2)]
    for i in range (len(inputs)):
        testList(inputs[i])
        
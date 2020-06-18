import argparse

def ruler(number):
    output1 = ""
    output2 = ""
    output3 = ""
    row1count = int(number/10)
    row2count = int(number%10)

    for i in range(row1count):
        output1 += " "*9 + str(i+1)

    for i in range(row1count):
        for i in range(10):
            if(i+1 != 10):
                output2 += str(i+1)
            else:
                output2 = output2 + "0"
    for i in range(row2count):
        output3 += str(i+1)


    return output1 + "\n" + output2 + output3
if __name__ == ""__main__":
    parser = argparse.ArgumentParser()
    parser.add_argement("number")
    args = parser.parser_args()
    number = args.number
    try:
        print(ruler(int(number)))
    except Exception as e:
        print("Exception occured, please pass intefer value argument")
        
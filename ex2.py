import argparse

def isWhiteLine(line):
    if line.strip() !="":
        return line
    elif line.strip() =="":
        return True
    elif " " and '\t' in line:
        return True
    elif line in ['\n', '\r\n']:
        return True

    else:
        return line

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parser_args()
    filename = args.filename
    with open(args.filename, "r") as file:
        for line in file:
            print(isWhiteLine(line))

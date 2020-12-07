import xlrd
import sys
import getopt
import exceltest


def main(argv):
    inputfile = ''
    checktype = 0
    try:
        opts, args = getopt.getopt(argv, "hi:t:", ["ifile=", "t="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -t <checkType>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-t", "--t"):
            checktype = int(arg)
    print('输入的文件为：', inputfile)
    print('检查的类型为：', checktype)
    data = xlrd.open_workbook(inputfile)
    if checktype == 0:
        return exceltest.checkBegin(data)
    elif checktype == 1:
        return exceltest.checkSprint1(data)
    elif checktype == 2:
        return exceltest.checkSprint2(data)
    elif checktype == 3:
        return exceltest.checkEnd(data)
    else:
        print("invalid type")
        return False


if __name__ == "__main__":
    print("check result:", main(sys.argv[1:]))

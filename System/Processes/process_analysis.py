#import xlrd


#fileName = 'D:\\svn\\cmmi\\cmmi\\EPG工作库\\过程改进管理工作\\度量\\3-7项目度量表-力维.xlsx'
# file = xlrd.open_workbook(fileName)  # 打开xls文件

# table = file.sheet_by_name(r"过程分析")  # 打开第一张表


def checkCellValid(tab, row, col):
    if tab.cell(row, col).ctype == 0:
        return False
    else:
        return True


def checkStabilityBegin(tab):
    result = (not checkCellValid(tab, 3, 4)) \
        & (not checkCellValid(tab, 4, 4)) \
        & (not checkCellValid(tab, 5, 4)) \
        & (not checkCellValid(tab, 6, 4)) \
        & (not checkCellValid(tab, 3, 5)) \
        & (not checkCellValid(tab, 4, 5)) \
        & (not checkCellValid(tab, 5, 5)) \
        & (not checkCellValid(tab, 6, 5))
    if (not result):
        print("稳定性Begin:", result)
    return result


def checkStabilitySprint1(tab):
    result = checkCellValid(tab, 3, 4) \
        & checkCellValid(tab, 4, 4) \
        & checkCellValid(tab, 5, 4) \
        & checkCellValid(tab, 6, 4) \
        & (not checkCellValid(tab, 3, 5)) \
        & (not checkCellValid(tab, 4, 5)) \
        & (not checkCellValid(tab, 5, 5)) \
        & (not checkCellValid(tab, 6, 5))
    if (not result):
        print("稳定性Sprint1:", result)
    return result


def checkStabilitySprint2(tab):
    result = checkCellValid(tab, 3, 4) \
        & checkCellValid(tab, 4, 4) \
        & checkCellValid(tab, 5, 4) \
        & checkCellValid(tab, 6, 4) \
        & checkCellValid(tab, 3, 5) \
        & checkCellValid(tab, 4, 5) \
        & checkCellValid(tab, 5, 5) \
        & checkCellValid(tab, 6, 5)
    if (not result):
        print("稳定性Sprint2:", result)
    return result


def checkStabilityEnd(tab):
    result = checkStabilitySprint2(tab)
    if (not result):
        print("稳定性End:", result)
    return result


def checkPerformanceBegin(tab):
    result = (not checkCellValid(tab, 12, 4)) \
        & (not checkCellValid(tab, 13, 4)) \
        & (not checkCellValid(tab, 14, 4)) \
        & (not checkCellValid(tab, 15, 4)) \
        & (not checkCellValid(tab, 12, 5)) \
        & (not checkCellValid(tab, 13, 5)) \
        & (not checkCellValid(tab, 14, 5)) \
        & (not checkCellValid(tab, 15, 5))
    if (not result):
        print("能力Begin:", result)
    return result


def checkPerformanceSprint1(tab):
    result = checkCellValid(tab, 12, 4) \
        & checkCellValid(tab, 13, 4) \
        & checkCellValid(tab, 14, 4) \
        & checkCellValid(tab, 15, 4) \
        & (not checkCellValid(tab, 12, 5)) \
        & (not checkCellValid(tab, 13, 5)) \
        & (not checkCellValid(tab, 14, 5)) \
        & (not checkCellValid(tab, 15, 5))
    if (not result):
        print("能力Sprint1:", result)
    return result


def checkPerformanceSprint2(tab):
    result = checkCellValid(tab, 12, 4) \
        & checkCellValid(tab, 13, 4) \
        & checkCellValid(tab, 14, 4) \
        & checkCellValid(tab, 15, 4) \
        & checkCellValid(tab, 12, 5) \
        & checkCellValid(tab, 13, 5) \
        & checkCellValid(tab, 14, 5) \
        & checkCellValid(tab, 15, 5)
    if (not result):
        print("能力Sprint2:", result)
    return result


def checkPerformanceEnd(tab):
    result = checkPerformanceSprint2(tab)
    if (not result):
        print("能力End:", result)
    return result


def checkProcessAnalysisBegin(data):
    tab = data.sheet_by_name(r"过程分析")
    return checkPerformanceBegin(tab) & checkStabilityBegin(tab)


def checkProcessAnalysisSprint1(data):
    tab = data.sheet_by_name(r"过程分析")
    return checkPerformanceSprint1(tab) & checkStabilitySprint1(tab)


def checkProcessAnalysisSprint2(data):
    tab = data.sheet_by_name(r"过程分析")
    return checkPerformanceSprint2(tab) & checkStabilitySprint2(tab)


def checkProcessAnalysisEnd(data):
    tab = data.sheet_by_name(r"过程分析")
    return checkPerformanceEnd(tab) & checkStabilityEnd(tab)

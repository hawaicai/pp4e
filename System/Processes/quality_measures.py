#import xlrd


#fileName = 'D:\\svn\\cmmi\\cmmi\\EPG工作库\\过程改进管理工作\\度量\\3-7项目度量表-力维.xlsx'
# file = xlrd.open_workbook(fileName)  # 打开xls文件

# table = file.sheet_by_name(r"质量度量")  # 打开第一张表


def checkCellValid(tab, row, col):
    if tab.cell(row, col).ctype == 0:
        return False
    else:
        return True


def checkCodeReviewBegin(tab):
    result = (not checkCellValid(tab, 3, 5)) & (not checkCellValid(
        tab, 3, 6)) & checkCellValid(tab, 4, 5) & checkCellValid(tab, 4, 6)
    if (not result):
        print("代码评审缺陷密度Begin:", result)
    return result


def checkCodeReviewSprint1(tab):
    result = checkCellValid(tab, 3, 5) & (not checkCellValid(
        tab, 3, 6)) & checkCellValid(tab, 4, 5) & checkCellValid(tab, 4, 6)
    if (not result):
        print("代码评审缺陷密度Sprint1:", result)
    return result


def checkCodeReviewSprint2(tab):
    result = checkCellValid(tab, 3, 5) & checkCellValid(
        tab, 3, 6) & checkCellValid(tab, 4, 5) & checkCellValid(tab, 4, 6)
    if (not result):
        print("代码评审缺陷密度Sprint2:", result)
    return result


def checkCodeReviewEnd(tab):
    result = checkCodeReviewSprint2(tab)
    if (not result):
        print("代码评审缺陷密度End:", result)
    return result


def checkTestCaseDensityBegin(tab):
    result = (not checkCellValid(tab, 18, 5)) & (
        not checkCellValid(tab, 18, 6))
    if (not result):
        print("测试用例密度Begin:", result)
    return result


def checkTestCaseDensitySprint1(tab):
    result = checkCellValid(tab, 18, 5) & (not checkCellValid(tab, 18, 6))
    if (not result):
        print("测试用例密度Sprint1:", result)
    return result


def checkTestCaseDensitySprint2(tab):
    result = checkCellValid(tab, 18, 5) & checkCellValid(tab, 18, 6)
    if (not result):
        print("测试用例密度Sprint2:", result)
    return result


def checkTestCaseDensityEnd(tab):
    result = checkTestCaseDensitySprint2(tab)
    if (not result):
        print("测试用例密度End:", result)
    return result


def checkReleaseDefectDensityBegin(tab):
    result = (not checkCellValid(tab, 33, 4)) & (
        not checkCellValid(tab, 33, 5))
    if (not result):
        print("现场缺陷密度Begin:", result)
    return result


def checkReleaseDefectDensitySprint1(tab):
    return checkReleaseDefectDensityBegin(tab)


def checkReleaseDefectDensitySprint2(tab):
    return checkReleaseDefectDensityBegin(tab)


def checkReleaseDefectDensityEnd(tab):
    result = checkCellValid(tab, 33, 4) & checkCellValid(tab, 33, 5)
    if (not result):
        print("现场缺陷密度End:", result)
    return result


def checkQualityMeasureBegin(data):
    tab = data.sheet_by_name(r"质量度量")
    return checkCodeReviewBegin(tab) & checkReleaseDefectDensityBegin(tab) & checkTestCaseDensityBegin(tab)


def checkQualityMeasureSprint1(data):
    tab = data.sheet_by_name(r"质量度量")
    return checkCodeReviewSprint1(tab) & checkReleaseDefectDensitySprint1(tab) & checkTestCaseDensitySprint1(tab)


def checkQualityMeasureSprint2(data):
    tab = data.sheet_by_name(r"质量度量")
    return checkCodeReviewSprint2(tab) & checkReleaseDefectDensitySprint2(tab) & checkTestCaseDensitySprint2(tab)


def checkQualityMeasureEnd(data):
    tab = data.sheet_by_name(r"质量度量")
    return checkCodeReviewEnd(tab) & checkReleaseDefectDensityEnd(tab) & checkTestCaseDensityEnd(tab)

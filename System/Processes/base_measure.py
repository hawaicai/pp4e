#import xlrd


#fileName = 'D:\\svn\\cmmi\\cmmi\\EPG工作库\\过程改进管理工作\\度量\\3-7项目度量表-力维.xlsx'
# file = xlrd.open_workbook(fileName)  # 打开xls文件

# table = file.sheet_by_name(r"基本度量")  # 打开第一张表


def checkCellValid(tab, row, col):
    if tab.cell(row, col).ctype == 0:
        return False
    else:
        return True


def checkProjectInfoValid(tab):
    result = checkCellValid(tab, 3, 3) & checkCellValid(
        tab, 4, 3) & checkCellValid(tab, 5, 3)
    if (not result):
        print("项目基本信息:", result)
    return result


def checkProjectTeamValid(tab):
    result = checkCellValid(tab, 13, 5) & checkCellValid(
        tab, 13, 6) & checkCellValid(tab, 14, 5) & checkCellValid(tab, 14, 6)
    if (not result):
        print("项目团队信息:", result)
    return result


def checkProjectMemberBegin(tab):
    result = (not checkCellValid(tab, 28, 5)) & (not checkCellValid(tab, 29, 5)) & (
        not checkCellValid(tab, 28, 6)) & (not checkCellValid(tab, 29, 6))
    if (not result):
        print("项目人员信息Begin:", result)
    return result


def checkProjectMemberSprint1(tab):
    result = (checkCellValid(tab, 28, 5)) & (checkCellValid(tab, 29, 5)) & (
        not checkCellValid(tab, 28, 6)) & (not checkCellValid(tab, 29, 6))
    if (not result):
        print("项目人员信息Sprint1:", result)
    return result


def checkProjectMemberSprint2(tab):
    result = (checkCellValid(tab, 28, 5)) & (checkCellValid(tab, 29, 5)) & (
        checkCellValid(tab, 28, 6)) & (checkCellValid(tab, 29, 6))
    if (not result):
        print("项目人员信息Sprint2:", result)
    return result


def checkProjectMemberEnd(tab):
    result = checkProjectMemberSprint2(tab)
    if (not result):
        print("项目人员信息End:", result)
    return result


def checkProjectRequimentsBegin(tab):
    result = checkCellValid(tab, 44, 6) & checkCellValid(tab, 44, 7) & (
        not checkCellValid(tab, 45, 6)) & (not checkCellValid(tab, 45, 7))
    if (not result):
        print("需求任务规划Begin:", result)
    return result


def checkProjectRequimentsSprint1(tab):
    result = checkCellValid(tab, 44, 6) & checkCellValid(
        tab, 44, 7) & checkCellValid(tab, 45, 6) & (not checkCellValid(tab, 45, 7))
    if (not result):
        print("需求任务规划Sprint1:", result)
    return result


def checkProjectRequimentsSprint2(tab):
    result = checkCellValid(tab, 44, 6) & checkCellValid(
        tab, 44, 7) & checkCellValid(tab, 45, 6) & checkCellValid(tab, 45, 7)
    if (not result):
        print("需求任务规划Sprint2:", result)
    return result


def checkProjectRequimentsEnd(tab):
    result = checkProjectRequimentsSprint2(tab)
    if (not result):
        print("需求任务规划End:", result)
    return result


def checkProjectVelocityBegin(tab):
    result = (not checkCellValid(tab, 54, 6)) & (
        not checkCellValid(tab, 54, 7))
    if (not result):
        print("迭代速率Begin:", result)
    return result


def checkProjectVelocitySprint1(tab):
    result = checkCellValid(tab, 54, 6) & (not checkCellValid(tab, 54, 7))
    if (not result):
        print("迭代速率Sprint1:", result)
    return result


def checkProjectVelocitySprint2(tab):
    result = checkCellValid(tab, 54, 6) & checkCellValid(tab, 54, 7)
    if (not result):
        print("迭代速率Sprint2:", result)
    return result


def checkProjectVelocityEnd(tab):
    result = checkProjectVelocitySprint2(tab)
    if (not result):
        print("迭代速率End:", result)
    return result


def checkProjectWorkloadBegin(tab):
    result = checkCellValid(tab, 62, 6) & checkCellValid(tab, 62, 7)
    if (not result):
        print("工作量统计项目有效人天Begin:", result)
    return result


def checkProjectWorkloadSprint1(tab):
    return checkProjectWorkloadBegin(tab)


def checkProjectWorkloadSprint2(tab):
    return checkProjectWorkloadBegin(tab)


def checkProjectWorkloadEnd(tab):
    return checkProjectWorkloadBegin(tab)


def checkBaseMeasureBegin(data):
    tab = data.sheet_by_name(r"基本度量")
    return checkProjectInfoValid(tab)\
        & checkProjectMemberBegin(tab)\
        & checkProjectRequimentsBegin(tab)\
        & checkProjectTeamValid(tab)\
        & checkProjectVelocityBegin(tab)\
        & checkProjectWorkloadBegin(tab)


def checkBaseMeasureSprint1(data):
    tab = data.sheet_by_name(r"基本度量")
    return checkProjectInfoValid(tab)\
        & checkProjectMemberSprint1(tab)\
        & checkProjectRequimentsSprint1(tab)\
        & checkProjectTeamValid(tab)\
        & checkProjectVelocitySprint1(tab)\
        & checkProjectWorkloadSprint1(tab)


def checkBaseMeasureSprint2(data):
    tab = data.sheet_by_name(r"基本度量")
    return checkProjectInfoValid(tab)\
        & checkProjectMemberSprint2(tab)\
        & checkProjectRequimentsSprint2(tab)\
        & checkProjectTeamValid(tab)\
        & checkProjectVelocitySprint2(tab)\
        & checkProjectWorkloadSprint2(tab)


def checkBaseMeasureEnd(data):
    tab = data.sheet_by_name(r"基本度量")
    return checkProjectInfoValid(tab)\
        & checkProjectMemberEnd(tab)\
        & checkProjectRequimentsEnd(tab)\
        & checkProjectTeamValid(tab)\
        & checkProjectVelocityEnd(tab)\
        & checkProjectWorkloadEnd(tab)

import xlrd
import base_measure
import quality_measures
import process_analysis


#fileName = 'D:\\svn\\cmmi\\cmmi\\EPG工作库\\过程改进管理工作\\度量\\3-7项目度量表-力维.xlsx'
# 打开xls文件


def checkBegin(file):
    result = base_measure.checkBaseMeasureBegin(file) \
        & quality_measures.checkQualityMeasureBegin(file) \
        & process_analysis.checkProcessAnalysisBegin(file)
    if (not result):
        print("迭代1计划:", result)
    return result


def checkSprint1(file):
    result = base_measure.checkBaseMeasureSprint1(file) \
        & quality_measures.checkQualityMeasureSprint1(file) \
        & process_analysis.checkProcessAnalysisSprint1(file)
    if (not result):
        print("迭代2计划:", result)
    return result


def checkSprint2(file):
    result = base_measure.checkBaseMeasureSprint2(file) \
        & quality_measures.checkQualityMeasureSprint2(file) \
        & process_analysis.checkProcessAnalysisSprint2(file)
    if (not result):
        print("迭代2完成:", result)
    return result


def checkEnd(file):
    result = base_measure.checkBaseMeasureEnd(file) \
        & quality_measures.checkQualityMeasureEnd(file) \
        & process_analysis.checkProcessAnalysisEnd(file)
    if (not result):
        print("迭代结束:", result)
    return result

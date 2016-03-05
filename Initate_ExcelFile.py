__author__ = 'liujunyuan'
import xlrd
import xlwt
import calendar

print "enter the Year:"
theYear = input()
print "enter the Month:"
theMonth = input()

def openExcel():
    global theYear
    global theMonth
    if theMonth<10:
        filename = ("CLD"+ str(theYear) + str(0) + str(theMonth))
    else:
        filename = ("CLD"+ str(theYear)  + str(theMonth))
    excelfile = xlrd.open_workbook("/Users/liujunyuan/Desktop/" + filename + ".xls" )
    return excelfile

def getIterator():
    global theYear
    global theMonth
    monthRange = calendar.monthrange(theYear ,theMonth)
    return monthRange[1]

def theOutput():
    global theMonth
    global theYear
    result = xlwt.Workbook()
    sheet = result.add_sheet(str(theYear)+str(theMonth) ,cell_overwrite_ok= True)
    sheet.write(0,0,'day')
    sheet.write(0,1,'year')
    sheet.write(0,2,'hour')
    sheet.write(0,3,'T')
    sheet.write(0,4,'U')
    sheet.write(0,5,'radiation')
    sheet.write(0,6,'RH')
    sheet.write(0,7,'PAR')
    sheet.write(0,8,'rain')
    result.save('/Users/liujunyuan/Desktop/'+ str(theYear) + '.xls')
    outputfile = xlrd.open_workbook('/Users/liujunyuan/Desktop/'+ str(theYear) + '.xls')
    return outputfile

def getData():
    # targetsheet  = theOutput().sheet_by_name(str(theYear)+str(theMonth))
    formerdata = openExcel().sheet_by_name('T')
    
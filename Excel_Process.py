__author__ = 'liujunyuan'
import xlrd
import xlwt
import calendar


thisYear = 2010
month_seq = ['01','02','03']
month_seq1 = ['01','02','03','04','05','06','07','08','09','10','11','12']

workbook = xlwt.Workbook()
worksheet = workbook.add_sheet("year"+str(thisYear),cell_overwrite_ok= True)
worksheet.write(0,0,'day')
worksheet.write(0,1,'year')
worksheet.write(0,2,'hour')
worksheet.write(0,3,'T')
worksheet.write(0,4,'U')
worksheet.write(0,5,'radiation')
worksheet.write(0,6,'E-pan')
worksheet.write(0,7,'RH')
worksheet.write(0,8,'PAR')
worksheet.write(0,9,'rain')
beginfrom = 0

for thisMonth in month_seq1:
    excelfile = xlrd.open_workbook("/Users/liujunyuan/Desktop/" + "CLD"+ str(thisYear) + str(thisMonth) + ".xls" )
    monthRange = calendar.monthrange(thisYear,int(thisMonth))[1]
    D_sheet_name = ['D51', 'D52', 'D53', 'D54', 'D55', 'D56', 'D57', 'D58', 'D59', 'D510', 'D511', 'D512', 'D513', 'D514',
                'D515', 'D516', 'D517', 'D518', 'D519', 'D520', 'D521', 'D522', 'D523', 'D524', 'D525', 'D526', 'D527',
                'D528', 'D529', 'D530', 'D531']
    del D_sheet_name[monthRange:32]
    sheet = excelfile.sheet_by_name("T")
    sheet_RH = excelfile.sheet_by_name("RH")
    sheet_W10A = excelfile.sheet_by_name("W10A")
    sheet_R = excelfile.sheet_by_name("R")
    sequence = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,1,2,3,4]


    for j in range(beginfrom,beginfrom + monthRange ,1):
        for i in sequence:
            time = sheet.cell(4,i).value
            day = sheet.cell(j-beginfrom+5,0).value
            par_T = sheet.cell(j-beginfrom+5,i).value
            par_W10A = sheet_W10A.cell(6+2*(j-beginfrom),i+1).value
            par_RH = sheet_RH .cell(j-beginfrom+5,i).value
            par_R = sheet_R .cell(j-beginfrom+5,i).value
            par_Eg = excelfile.sheet_by_name(D_sheet_name[j-beginfrom]).cell(sequence.index(i)+5,1).value
            par_PAR = excelfile.sheet_by_name(D_sheet_name[j-beginfrom]).cell(sequence.index(i)+5,5).value

            row = sequence.index(i)+1
            worksheet.write(row+24*j,0,day+beginfrom)
            worksheet.write(row+24*j,1,thisYear)
            worksheet.write(row+24*j,2,time)
            worksheet.write(row+24*j,3,par_T)
            worksheet.write(row+24*j,4,par_W10A)
            worksheet.write(row+24*j,5,par_Eg)
            worksheet.write(row+24*j,7,par_RH)
            worksheet.write(row+24*j,8,par_PAR)
            worksheet.write(row+24*j,9,par_R)
    beginfrom = beginfrom + monthRange

workbook.save('/Users/liujunyuan/Desktop/2010_untested.xls')





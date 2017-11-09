# coding:utf-8
import traceback
from PyPDF2 import PdfFileReader

# 参数为pdf文件全路径名
def isValidPDF_pathfile(pathfile):
    bValid = True
    try:
        PdfFileReader(open(pathfile, 'rb'))
        reader = PdfFileReader(pathfile)
        if reader.getNumPages() < 1:  # 进一步通过页数判断。
            bValid = False
    except:
        bValid = False
        print('*' + traceback.format_exc())

    return bValid

# print("1203943984.PDF",isValidPDF_pathfile('pdf/1203943984.PDF'))
# print("60931440.PDF",isValidPDF_pathfile('pdf/60931440.PDF'))
print("10241903.PDF",isValidPDF_pathfile('pdf/10241903.PDF'))
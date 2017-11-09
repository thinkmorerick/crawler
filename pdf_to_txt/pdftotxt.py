# coding:utf-8
import traceback

import os
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open
try:
    os.mkdir('./txt')
except:
    pass

def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)

    process_pdf(rsrcmgr, device, pdfFile)
    device.close()

    content = retstr.getvalue()
    retstr.close()
    return content


def saveTxt(txt):
    with open("txt/15166020.txt", "w") as f:
        f.write(txt)

try:
    txt = readPDF(open('pdf/15166020.PDF', 'rb'))
    saveTxt(txt)

except:
    print("15166020.PDF cannot convert to txt!!")
    traceback.print_exc()

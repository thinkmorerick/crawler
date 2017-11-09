# coding:utf-8

import datetime
import math
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open
import glob
import os

# 创建目标目录
try:
    os.mkdir('./output_txt')
    os.mkdir('./output_log')
except:
    pass

# 打开所有文件
def open_allfile(path,filetype):
    data=[]
    read_files=glob.glob(path+'*'+filetype)
    for i in read_files:
        with open(i,'rb') as infile:
            data.append(infile.read())
    return data

# 获取文件名称
def get_filename(path,filetype):
    import os
    name=[]
    for root,dirs,files in os.walk(path):
        for i in files:
            if filetype in i:
                name.append(i.replace(filetype,''))
    return name

# 读取PDF文件
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

# 保存TXT文件
def saveTxt(txt,name):
    with open("output_txt/"+name+".txt", "w") as f:
        f.write(txt)

# 保存Error日志
def saveErrorLog(content):
    with open("output_log/errorlist.log", "a") as f:
        f.write(content)

# 保存Success日志
def saveSuccessLog(content):
    with open("output_log/successlist.log", "a") as f:
        f.write(content)

# 保存全部列表日志
def saveTotalListLog(content):
    with open("output_log/totallist.log", "a") as f:
        f.write(content)
# 时间转换
def changeTime(allTime):
    day = 24 * 60 * 60
    hour = 60 * 60
    min = 60
    if allTime < 60:
        return "%d sec" % math.ceil(allTime)
    elif allTime > day:
        days = divmod(allTime, day)
        return "%d days, %s" % (int(days[0]), changeTime(days[1]))
    elif allTime > hour:
        hours = divmod(allTime, hour)
        return '%d hours, %s' % (int(hours[0]), changeTime(hours[1]))
    else:
        mins = divmod(allTime, min)
        return "%d mins, %d sec" % (int(mins[0]), math.ceil(mins[1]))

# 计数器
errorCount = 0
successCount = 0
totolCount = 0

# 开始时间
startTime = datetime.datetime.now()
print ("startTime: ", str(startTime.strftime('%X')))
saveTotalListLog("startTime: " + str(startTime.strftime('%Y-%m-%d %H:%M:%S')) + "\n")
names=get_filename('pdf/','.PDF')

# 遍历转换并保存文件
for name in names:
    totolCount = totolCount + 1
    fpath = "pdf/"+name+".PDF"
    try:
        txt = readPDF(open(fpath, 'rb'))
        saveTxt(txt,name)
        successCount = successCount + 1
        saveSuccessLog(str(successCount) +": " + name+".PDF: converted to txt success. \n")
        saveTotalListLog(str(totolCount) +": " + name + ".PDF: converted to txt success. \n")
    except:
        errorCount = errorCount + 1
        print(str(errorCount) +": " + name+".PDF: failed converting to txt.")
        saveErrorLog(str(errorCount) +": " + name+".PDF: failed converting to txt. \n")
        saveTotalListLog(str(totolCount) +": " + name+".PDF: failed converting to txt. \n")

# 结束时间
endTime = datetime.datetime.now()
print ("endTime: ", str(endTime.strftime('%X')))
# 时间差
tt = (endTime - startTime).seconds
totalTime = changeTime(tt)
print("totalTime: " + str(totalTime))
saveTotalListLog("endTime: " + str(endTime.strftime('%Y-%m-%d %H:%M:%S')) + "\n")
saveTotalListLog("totalTime: " + str(totalTime) + "\n")


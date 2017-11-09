# coding: utf-8
import datetime
import traceback
import urllib
from urllib.request import urlopen


# 创建输出目录
import os

import math

try:
    os.mkdir('./output_pdf/')
    os.mkdir('./pdf_log/')
except:
    pass


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

print('开始检查：')
# 开始时间
startTime = datetime.datetime.now()
print("startTime: ", str(startTime.strftime('%X')))

#导入你的URL文件
addr = open('url_shanghai/1.txt')
for url in addr:
    # 给pdf命名
    path = url[url.rindex("/")+1:]
    print(path)
    # 打开URL
    data = urllib.request.urlopen(url).read()
    # 读取，写入资料文件夹
    try:
        f = open('output_pdf/'+path,"wb")
        f.write(data)
        f.close()
    except:
        e = open("pdf_log/error.log", 'a')
        traceback.print_exc(file=e)
        f.flush()
        f.close()

# 结束时间
endTime = datetime.datetime.now()
print ("endTime: ", str(endTime.strftime('%X')))
# 时间差
tt = (endTime - startTime).seconds
totalTime = changeTime(tt)
print("totalTime: " + str(totalTime))
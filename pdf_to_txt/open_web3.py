# coding:utf-8
import webbrowser
import time

# 每隔2小时执行一次，就会每隔2小时打开一次网页。
# time.sleep(10)
# total_breaks = 3
# break_count = 0

print("This program started on " + time.ctime())
# while(break_count < total_breaks):
# time.sleep(2)
webbrowser.open("http://www.pdfdo.com/pdf-remove-restriction.aspx")
    # break_count = break_count + 1
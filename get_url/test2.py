# # coding:utf-8
# import random
# import sys
# import pprint
# import importlib
#
# import time
#
# importlib.reload(sys)
# import requests
# urldict={}
# import os
# try:
#     os.mkdir('./output')
# except:
#     pass
# try:
#     #从巨潮资讯解析出pdf的真实下载地址
#     f=open('stkcd.csv','r')
#     fout=open('./output/urls.csv','a')
#     for line in f:
#         stkcd = str(line[:6])
#         s = requests.Session()
#         headers = {
#             'Host':'www.cninfo.com.cn',
#             'Origin':'http://www.cninfo.com.cn',
#             'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
#             'Accept':'application/json, text/javascript, */*; q=0.01'
#         }
#         postdata = {
#             'stock':stkcd,
#             'category':'category_ndbg_szsh;',
#             'pageNum':'1',
#             'pageSize':'30',
#             'column':'sse',
#             'searchkey':'年度报告',
#             'tabName':'tabName:fulltext'
#         }
#         url = "http://www.cninfo.com.cn/cninfo-new/announcement/query"
#         s.headers.update(headers)
#         r = s.post(url,data=postdata)
#         # print(r.text)
#         dict = r.json()
#         for i in dict['announcements']:
#             title = i['announcementTitle']
#             if '摘要' not in title:
#                 if '半' not in title:
#                     if '回复' not in title:
#                         if '书' not in title:
#                             if '公告' not in title:
#                                 if '说明' not in title:
#                                     if '意见' not in title:
#                                         if '回函' not in title:
#                                             if '答复' not in title:
#                                                 if '审计' not in title:
#                                                     if '董事会' not in title:
#                                                         if '复涵' not in title:
#                                                             if '问询' not in title:
#                                                                 if '审核' not in title:
#                                                                     if '声明' not in title:
#                                                                         if '董事' not in title:
#                                                                             if '管理' not in title:
#                                                                                 if '人员' not in title:
#                                                                                     if '总结' not in title:
#                                                                                         if '规程' not in title:
#                                                                                             if '人员' not in title:
#                                                                                                 if '年度报告' in title:
#                                                                                                     print(stkcd,title)
#                                                                                                     url = 'http://www.cninfo.com.cn/' + i['adjunctUrl']
#                                                                                                     # print(url)
#                                                                                                     secname = i['secName']
#                                                                                                     date = i['adjunctUrl'][10:20]
#                                                                                                     # title = title[(title.find("：") + 1):]
#                                                                                                     # title = title[0:title.find("<em>")] + title[(title.find("<em>") + 4):]
#                                                                                                     # title = title[0:title.find("</em>")]
#                                                                                                     urldict.update({stkcd + '-' + secname + '-' + title + '-' + date: url})
#                                                                                                     csvtowrite = stkcd + ',' + secname + ',' + title + ',' + date + ',' + url + '\n'
#                                                                                                     fout.write(csvtowrite)
#
#                                                                                                     # 控制访问间隔
#                                                                                                     # num = random.randint(0, 3)
#                                                                                                     # print(num)
#                                                                                                     # time.sleep(num)
#
#     fout.close()
# except:
#     print("第一页，卡住了。。。。")
# try:
#     f=open('stkcd1.csv','r')
#     fout=open('./output/urls1.csv','a')
#     for line in f:
#         stkcd = str(line[:6])
#         s = requests.Session()
#         headers = {
#             'Host':'www.cninfo.com.cn',
#             'Origin':'http://www.cninfo.com.cn',
#             'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
#             'Accept':'application/json, text/javascript, */*; q=0.01'
#         }
#         postdata = {
#             'stock':stkcd,
#             'category':'category_ndbg_szsh;',
#             'pageNum':'2',
#             'pageSize':'30',
#             'column':'sse',
#             'searchkey':'年度报告',
#             'tabName':'tabName:fulltext'
#         }
#         url = "http://www.cninfo.com.cn/cninfo-new/announcement/query"
#         s.headers.update(headers)
#         r = s.post(url,data=postdata)
#         # print(r.text)
#         dict = r.json()
#         for i in dict['announcements']:
#             title = i['announcementTitle']
#             if '摘要' not in title:
#                 if '半' not in title:
#                     if '回复' not in title:
#                         if '书' not in title:
#                             if '公告' not in title:
#                                 if '说明' not in title:
#                                     if '意见' not in title:
#                                         if '回函' not in title:
#                                             if '答复' not in title:
#                                                 if '审计' not in title:
#                                                     if '董事会' not in title:
#                                                         if '复涵' not in title:
#                                                             if '问询' not in title:
#                                                                 if '审核' not in title:
#                                                                     if '声明' not in title:
#                                                                         if '董事' not in title:
#                                                                             if '管理' not in title:
#                                                                                 if '人员' not in title:
#                                                                                     if '总结' not in title:
#                                                                                         if '规程' not in title:
#                                                                                             if '人员' not in title:
#                                                                                                 if '年度报告' in title:
#                                                                                                     print(stkcd,title)
#                                                                                                     url = 'http://www.cninfo.com.cn/' + i['adjunctUrl']
#                                                                                                     # print(url)
#                                                                                                     secname = i['secName']
#                                                                                                     date = i['adjunctUrl'][10:20]
#                                                                                                     # title = title[(title.find("：") + 1):]
#                                                                                                     # title = title[0:title.find("<em>")] + title[(title.find("<em>") + 4):]
#                                                                                                     # title = title[0:title.find("</em>")]
#                                                                                                     urldict.update({stkcd + '-' + secname + '-' + title + '-' + date: url})
#                                                                                                     csvtowrite = stkcd + ',' + secname + ',' + title + ',' + date + ',' + url + '\n'
#                                                                                                     fout.write(csvtowrite)
#
#                                                                                                     # 控制访问间隔
#                                                                                                     # num = random.randint(0, 3)
#                                                                                                     # print(num)
#                                                                                                     # time.sleep(num)
#     fout.close()
# except:
#     print("第二页，卡住了。。。。")
# try:
#     f=open('stkcd1.csv','r')
#     fout=open('./output/urls1.csv','a')
#     for line in f:
#         stkcd = str(line[:6])
#         s = requests.Session()
#         headers = {
#             'Host':'www.cninfo.com.cn',
#             'Origin':'http://www.cninfo.com.cn',
#             'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
#             'Accept':'application/json, text/javascript, */*; q=0.01'
#         }
#         postdata = {
#             'stock':stkcd,
#             'category':'category_ndbg_szsh;',
#             'pageNum':'3',
#             'pageSize':'30',
#             'column':'sse',
#             'searchkey':'年度报告',
#             'tabName':'tabName:fulltext'
#         }
#         url = "http://www.cninfo.com.cn/cninfo-new/announcement/query"
#         s.headers.update(headers)
#         r = s.post(url,data=postdata)
#         # print(r.text)
#         dict = r.json()
#         for i in dict['announcements']:
#             title = i['announcementTitle']
#             if '摘要' not in title:
#                 if '半' not in title:
#                     if '回复' not in title:
#                         if '书' not in title:
#                             if '公告' not in title:
#                                 if '说明' not in title:
#                                     if '意见' not in title:
#                                         if '回函' not in title:
#                                             if '答复' not in title:
#                                                 if '审计' not in title:
#                                                     if '董事会' not in title:
#                                                         if '复涵' not in title:
#                                                             if '问询' not in title:
#                                                                 if '审核' not in title:
#                                                                     if '声明' not in title:
#                                                                         if '董事' not in title:
#                                                                             if '管理' not in title:
#                                                                                 if '人员' not in title:
#                                                                                     if '总结' not in title:
#                                                                                         if '规程' not in title:
#                                                                                             if '人员' not in title:
#                                                                                                 if '年度报告' in title:
#                                                                                                     print(stkcd,title)
#                                                                                                     url = 'http://www.cninfo.com.cn/' + i['adjunctUrl']
#                                                                                                     # print(url)
#                                                                                                     secname = i['secName']
#                                                                                                     date = i['adjunctUrl'][10:20]
#                                                                                                     # title = title[(title.find("：") + 1):]
#                                                                                                     # title = title[0:title.find("<em>")] + title[(title.find("<em>") + 4):]
#                                                                                                     # title = title[0:title.find("</em>")]
#                                                                                                     urldict.update({stkcd + '-' + secname + '-' + title + '-' + date: url})
#                                                                                                     csvtowrite = stkcd + ',' + secname + ',' + title + ',' + date + ',' + url + '\n'
#                                                                                                     fout.write(csvtowrite)
#
#                                                                                                     # 控制访问间隔
#                                                                                                     # num = random.randint(0, 3)
#                                                                                                     # print(num)
#                                                                                                     # time.sleep(num)
#
#     fout.close()
#     # print("\n===========================")
#     # pprint.pprint(urldict)
#
#     #根据解析出的pdf地址下载到output，并重命名成有规律的文件
#     # import urllib2
#     # for name in urldict:
#     #     url=urldict[name]
#     #     response = urllib2.urlopen(url)
#     #     file = open('./output/'+name+".pdf", 'wb')
#     #     file.write(response.read())
#     #     file.close()
#     #     print name
# except:
#     print("第三页，卡住了。。。。")
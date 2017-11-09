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
#
# #从巨潮资讯解析出pdf的真实下载地址
# f=open('stkcd.csv','r')
# fout=open('./output/urls.csv','w')
# for line in f:
#     stkcd = str(line[:6])
#     # 这一行把“招股说明书”换成　“年报”　“半年报”　之类的，即可批量下载其他的公告
#     response=requests.get('http://www.cninfo.com.cn/cninfo-new/fulltextSearch/full?searchkey='+stkcd+'+年报&sdate=&edate=&isfulltext=false&sortName=nothing&sortType=desc&pageNum=1')
#     dict=response.json()
#     for i in dict['announcements']:
#         title=i['announcementTitle']
#         if '摘要' not in title:
#             if '半' not in title:
#                 if '回复' not in title:
#                     if '书' not in title:
#                         if '公告' not in title:
#                             if '说明' not in title:
#                                 if '意见' not in title:
#                                     if '回函' not in title:
#                                         if '答复' not in title:
#                                             if '审计' not in title:
#                                                 if '董事会' not in title:
#                                                     if '复涵' not in title:
#                                                         if '问询' not in title:
#                                                             if '审核' not in title:
#                                                                 if '年度报告' in title:
#                                                                     print(title)
#                                                                     url='http://www.cninfo.com.cn/'+i['adjunctUrl']
#                                                                     print(url)
#                                                                     secname=i['secName']
#                                                                     date=i['adjunctUrl'][10:20]
#                                                                     title=title[(title.find("：")+1):]
#                                                                     title=title[0:title.find("<em>")]+title[(title.find("<em>")+4):]
#                                                                     title=title[0:title.find("</em>")]
#                                                                     urldict.update({stkcd+'-'+secname+'-'+title+'-'+date:url})
#                                                                     csvtowrite=stkcd+','+secname+','+title+','+date+','+url+'\n'
#                                                                     fout.write(csvtowrite)
#
#                                                                     # 控制访问间隔
#                                                                     num = random.randint(0, 5)
#                                                                     print(num)
#                                                                     time.sleep(num)
#
# print("\n===========================")
# pprint.pprint(urldict)
# fout.close()
#
# #根据解析出的pdf地址下载到output，并重命名成有规律的文件
# # import urllib2
# # for name in urldict:
# #     url=urldict[name]
# #     response = urllib2.urlopen(url)
# #     file = open('./output/'+name+".pdf", 'wb')
# #     file.write(response.read())
# #     file.close()
# #     print name

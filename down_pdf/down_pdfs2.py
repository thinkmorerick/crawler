# coding: utf-8

import requests
from bs4 import BeautifulSoup
from urllib import parse
import re
import time
from multiprocessing import Pool

headers={
    'Host': 'www.cninfo.com.cn',
    'Connection': 'keep-alive',
    'Content-Length': '339',
    'Cache-Control': 'max-age=0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Origin': 'http://www.shclearing.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cookie': 'JSESSIONID=FAF72A420A385D8909C5B85C8A2E4B7A; cninfo_user_browse=000002,gssz0000002,%E4%B8%87%20%20%E7%A7%91%EF%BC%A1'
}

url1='http://www.cninfo.com.cn/cninfo-new/announcement/query'
url2=['http://www.cninfo.com.cn/cninfo-new/announcement/query'.format(str(i)) for i in range(1,5,1)]
url2.insert(0,url1)

links=[]
host='http://www.cninfo.com.cn/cninfo-new/announcement/query'
def get_link_list(url):
    for item in url:
        web_data=requests.get(item)
        soup=BeautifulSoup(web_data.text,'lxml')
        list=soup.select('ul.list li a')
        for item in list:
            link=host+item.get('href').split('./')[1]
            links.append(link)



FileName=[]
DownName=[]
DownName1=[]   #DownName1用于存放转码后的名称
def get_contents(link):
    web_data=requests.get(link)
    soup=BeautifulSoup(web_data.text,'lxml')
    contents=soup.select('#content > div.attachments > script')[0].get_text()
    a=str(re.findall(r"fileNames = '(.*?)'",contents,re.M)[0])
    b=str(re.findall(r"descNames = '(.*?)'",contents,re.M)[0])
    FileName=a.replace('./','').split(';;')
    DownName=b.split(';;')    #先用正则表达式提取出后面post中要用到的两个参数，但是要将中文转化为对应的URL编码
    for item in DownName:
        a=parse.quote(item)
        DownName1.append(a)
    print(FileName,'\\n',DownName,'\\n',DownName1)

    for i,j,k in zip(FileName,DownName1,DownName):
        download_file(i,j,k)

# link='http://www.shclearing.com/xxpl/fxpl/cp/201606/t20160608_159680.html'
# get_contents(link)
# print('The pdf have been downloaded successfully !')


def download_file(a,b,c):
    data={
        'FileName':a,
        'DownName':b }

    local_filename = "pdf2/"+c
    post_url='http://www.cninfo.com.cn/cninfo-new/announcement/query'
    time.sleep(0.5)  #限制下载的频次速度，以免被封
    # NOTE the stream=True parameter
    r = requests.post(post_url, data=data, headers=headers, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):  # 1024 是一个比较随意的数，表示分几个片段传输数据。
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                f.flush() #刷新也很重要，实时保证一点点的写入。
    return local_filename



if __name__=='__main__':
    get_link_list(url2)
    pool=Pool()
    pool.map(get_contents,links)
    print('The documents have been downloaded successfully !')

# 如果要将下载下来的文档的保存的路径存入mysql中，需要再加上下面的语句：
# conn=pymysql.connect(host='localhost',user='root',passwd='root',db='mysql',charset='utf8')
# cursor = conn.cursor()
# cursor.execute('CREATE TABLE root (id int auto_increment primary key,content varchar(100))')

# 以及在download_file(a,b,c)函数中的return local_filename语句前加上：
# cursor.execute('insert into root(content) values (%s)',local_filename)

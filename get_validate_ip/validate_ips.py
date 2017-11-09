import threading
import urllib.request

url = "http://quote.stockstar.com/stock"  #打算抓取内容的网页

proxy_ip={'http': '61.135.217.7:80'}  #想验证的代理IP

proxy_support = urllib.request.ProxyHandler(proxy_ip)

opener = urllib.request.build_opener(proxy_support)

opener.addheaders=[("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64)")]

urllib.request.install_opener(opener)

print(urllib.request.urlopen(url).read())


#多线程验证
threads=[]
for i in range(len(proxys)):
    thread=threading.Thread(target=test,args=[i])
    threads.append(thread)
    thread.start()
#阻塞主进程，等待所有子线程结束
for thread in threads:
    thread.join()
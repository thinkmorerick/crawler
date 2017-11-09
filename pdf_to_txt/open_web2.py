# coding:utf-8

from selenium import webdriver

# url = "http://www.eshow365.com/zhanhui/html/120062_0.html"
url = "http://www.pdfdo.com/pdf-remove-restriction.aspx"
# 这个路径就是你添加到PATH的路径
driver = webdriver.PhantomJS(executable_path='/Users/data/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')
driver.get(url)
print (driver.page_source)
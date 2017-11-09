from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('http://www.pdfdo.com/pdf-remove-restriction.aspx')
assert '百度' in browser.title

elem = browser.find_element_by_name('wd')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)  # 模拟按键

# browser.quit()
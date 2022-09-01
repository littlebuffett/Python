from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import subprocess

p1 = subprocess.Popen('chrome.exe --remote-debugging-port=9222 --user-data-dir="C:/ChromeTEMP"', cwd="C:/Program Files/Google/Chrome/Application/" ,shell=True)
print(p1)

time.sleep(2)

product_url = input('상품 url을 입력하세요:')

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_driver = r"C:\Users\Kang\Desktop\PythonWorkspace\web_scraping\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, options= chrome_options)
driver.get(product_url)

time.sleep(2)

driver.execute_script("window.scrollBy(0, 1000);") # 스크롤

driver.find_element(By.XPATH,'//*[@id="btfTab"]/ul[1]/li[2]').click()

reviews = []
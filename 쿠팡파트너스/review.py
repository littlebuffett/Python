from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import subprocess


def get_review(product_url):

    p1 = subprocess.Popen('chrome.exe --remote-debugging-port=9222 --user-data-dir="C:/ChromeTEMP"', cwd="C:/Program Files/Google/Chrome/Application/" ,shell=True)
    print(p1)

    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    chrome_driver = r'C:\Users\Study\Desktop\PythonWorkspace\chromedriver.exe'
    driver = webdriver.Chrome(chrome_driver, options= chrome_options)
    driver.get(product_url)

    time.sleep(2)

    driver.execute_script("window.scrollBy(0, 1000);") # 스크롤

    driver.find_element(By.XPATH,'//*[@id="btfTab"]/ul[1]/li[2]').click() # 상품평 버튼

    time.sleep(2)

    review = driver.find_element(By.XPATH, '//*[@id="btfTab"]/ul[2]/li[2]/div/div[6]/section[4]/article[1]/div[4]/div').text

    # print(review)

    return review
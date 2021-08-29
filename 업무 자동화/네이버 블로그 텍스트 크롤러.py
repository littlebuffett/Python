import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

url = input('글의 url 주소를 입력해주세요:')

html = urllib.request.urlopen(url).read() #html 문서 받아오기
soup = BeautifulSoup( html, 'html.parser') 

#iframe 벗기기.
iframexx = soup.find('iframe') 
real_url = 'https://blog.naver.com/' + iframexx.attrs['src']

real_html = urllib.request.urlopen(real_url).read()
real_soup = BeautifulSoup(real_html,'html.parser')

title = real_soup.find(class_='se-module se-module-text se-title-text').get_text()

content = real_soup.find(class_='se-main-container').find_all(class_='se-module se-module-text')

for i in content:
    print(i.get_text())

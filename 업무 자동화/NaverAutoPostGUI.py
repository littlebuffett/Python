from tkinter import *
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

#url을 입력하면 블로그 글을 가져오는 함수.
def getNaverBlogPost(url):
    html = urllib.request.urlopen(url).read() #html 문서 받아오기
    soup = BeautifulSoup( html, 'html.parser') 

    #iframe 벗기기.
    iframexx = soup.find('iframe') 
    real_url = 'https://blog.naver.com/' + iframexx.attrs['src']

    real_html = urllib.request.urlopen(real_url).read()
    real_soup = BeautifulSoup(real_html,'html.parser')

    title = real_soup.find(class_='se-module se-module-text se-title-text').get_text()

    print(title)

    content = real_soup.find(class_='se-main-container').find_all(class_='se-module se-module-text')

    for i in content:
        print(i.get_text())

    return content

def btncmd():   # btncomd 함수 설정
    text = getNaverBlogPost(url.get())
    for i in text:
        post.insert(END, i.get_text())
    print("글을 가져왔습니다!")
    
    
def reset():
    url.delete(0,END)
    post.delete("1.0",END)
    print("초기화 했습니다.")
    
def copyToClip():
    #root.withdraw()
    root.clipboard_clear()
    root.clipboard_append(post.get("1.0","end")) #1.0은 텍스트 위젯의 첫 번째 문자의 위치, end 맨 마지막 문자의 위치.
    #root.update()

root = Tk()
root.title("AutoPost")
root.geometry("800x750") # 가로 x 세로

guide = Label(root, width=100, height=3, text = "url을 입력해주세요.")
guide.pack()

url = Entry(root, width=50) #한 줄만 입력가능
url.pack()

post = Text(root, width=100, height= 40)
post.pack(pady=15)

btn_extract = Button(root, padx=10, pady=5, text="글 가져오기", command=btncmd)
btn_extract.pack(side="left",padx=50) #객체 생성후 루트에 포함하기

btn_copy = Button(root, padx=10, pady=5, text="복사", command=copyToClip)
btn_copy.pack(side="left")

btn_delete = Button(root, padx=10, pady=5, text="초기화", command=reset)
btn_delete.pack(side="left",padx=100)

root.mainloop()
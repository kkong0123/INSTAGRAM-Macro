from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from selenium import webdriver
from random import randint
import random
import time
import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import *

#UI파일 연결
base_dir = os.path.dirname(os.path.abspath(__file__))
form_class = uic.loadUiType(base_dir + "//insta.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.start_pushButton.clicked.connect(self.main)


    def main(self):
        global instagram_id
        global instagram_pwd
        global search_tag
        # global driver
        global start_time

##################################################

        instagram_id = self.lineEdit_id.text()
        instagram_pwd = self.lineEdit_pw.text()
        search_tag = self.lineEdit_tag.text()

        print(instagram_id)
        print(instagram_pwd)
        print(search_tag)
##################################################

        start_time = time.time() # 시작시간

        login()
        search()
        global i_cnt
        for i_cnt in range(400):
           
            follow_text = driver.find_element_by_css_selector("._aar2 ._aade").text
            if follow_text == "팔로우":
                like()
                comment()
                follow()
                # 다음 버튼 누르기
                driver.find_element_by_css_selector("._aaqg ._abl-").click()
                print('[' + time.strftime('%H:%M:%S') + ']' ,"다음 게시물 이동 중..\n =======================================")
                print("======= 총 경과시간 =======")
                print(elapsedTime())
                driver.implicitly_wait(30)
                time.sleep(random.uniform(3,6))

            else:
                print('[' + time.strftime('%H:%M:%S') + ']' ,"[이미 팔로우한 유저입니다]\n{0}번째 작업 건너뛰기".format(i_cnt+1))
                time.sleep(random.uniform(3,6))
                driver.find_element_by_css_selector("._aaqg ._abl-").click()
                print('[' + time.strftime('%H:%M:%S') + ']' ,"다음 게시물 이동 중..\n =======================================")
                print("======= 총 경과시간 =======")
                print(elapsedTime())            
                driver.implicitly_wait(30)
                time.sleep(random.uniform(3,6))

        
def login():
    global driver
    if getattr(sys, 'frozen', False):
        chromedriver_path = os.path.join(sys._MEIPASS, "./chromedriver")
        driver = webdriver.Chrome(chromedriver_path)
    else:
        driver = webdriver.Chrome('./chromedriver')

    url = 'https://www.instagram.com/accounts/login/'   
    driver.get(url)
    driver.implicitly_wait(15)
    print(elapsedTime())

    driver.find_element_by_css_selector(".-MzZI:nth-child(1) .zyHYP").send_keys(instagram_id)
    print('[' + time.strftime('%H:%M:%S') + ']' ,"id 입력 완료")
    time.sleep(random.uniform(10,15))
    driver.find_element_by_css_selector(".-MzZI+ .-MzZI .zyHYP").send_keys(instagram_pwd)
    print('[' + time.strftime('%H:%M:%S') + ']' ,"password 입력 완료") 
    time.sleep(random.uniform(5,10))
    driver.find_element_by_css_selector(".-MzZI+ .DhRcB").click()
    driver.implicitly_wait(15)
    time.sleep(5)
    print('[' + time.strftime('%H:%M:%S') + ']' ,"로그인 성공")

    ###
    print("== 경과시간 ==")
    print(elapsedTime())
    ###
    
    

def search():
    
    url = 'https://www.instagram.com/explore/tags/' + search_tag
    driver.get(url)
    driver.implicitly_wait(15)
    print('[' + time.strftime('%H:%M:%S') + ']' ,"해시태그 검색 중..")
    time.sleep(5)

    pic_list = driver.find_elements_by_css_selector("._aagw , ._aanf:nth-child(1) ._a6hd")
    pic_list = list(pic_list)
    driver.implicitly_wait(15)
    time.sleep(5)
    pic_list[0].click()
    driver.implicitly_wait(15)
    time.sleep(5)

    # 인기게시물 건너뛰기
    for i in range(9):
        driver.find_element_by_css_selector("._aaqg ._abl-").click()
        print('[' + time.strftime('%H:%M:%S') + ']' ,"{0}번째 인기 게시물 건너뛰기".format(i+1))
        driver.implicitly_wait(15)
        time.sleep(5)


def like():

    # #####
    # time.sleep(random.uniform(60,80))
    # #####

    driver.find_element_by_css_selector("._aamw ._abl-").click() # 좋아요 누르기
    print('[' + time.strftime('%H:%M:%S') + ']' ,"{}번째 좋아요".format(i_cnt+1))
    time.sleep(random.uniform(3,6))

def comment():

    driver.find_element_by_css_selector("._aaoc").click()
    time.sleep(random.uniform(1,5))

    # #####
    # time.sleep(random.uniform(60,90))
    # #####

    random_message = randomMessage() # 랜덤메시지 함수 리턴값 가져오기

    driver.find_element_by_css_selector("._aaoc").send_keys(random_message)
    time.sleep(random.uniform(1,5))

    # ######
    # time.sleep(random.uniform(60,80))
    # ######

    driver.find_element_by_css_selector("._aad0").click()
    print('[' + time.strftime('%H:%M:%S') + ']' ,"{0}번째 댓글입력: {1}".format(i_cnt+1, random_message))
    driver.implicitly_wait(15)
    time.sleep(random.uniform(4,6))

def follow():
    # #####
    # time.sleep(random.uniform(60,80))
    # #####

    driver.find_element_by_css_selector("._aar2 ._aade").click()
    print('[' + time.strftime('%H:%M:%S') + ']' ,"{0}번째 팔로우".format(i_cnt+1))
    time.sleep(random.uniform(7,12))

def randomMessage():

    random_message = [  
    "잘 보고갑니다! : )",
    "피드 잘 보고갑니다! :D",
    "피드 구경 잘 하고갑니다! : ) ",
    "게시물 잘보고갑니당! :)",
    "잘 보고갑니당! 맞팔해요!:D",
    "피드 구경 잘 하고 갑니다! 맞팔해용 :)",
    "피드가 너무 예뻐요 :) 맞팔해요!",
    "게시물 잘보고갑니당! 맞팔해요 :D"
    ]

    random_message = random_message[randint(0,7)]
    return random_message

def elapsedTime(): # 경과시간 정보 함수
    elapsed_time = time.time() - start_time
    m, s = divmod(elapsed_time, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    if d > 0:
        dtime = str(int(d)) + "일 "
    else: 
        dtime = ""
        
    if h > 0:
        htime = str(int(h)) + "시간 "
    else:
        htime = ""
        
    if m > 0:
        mtime = str(int(m)) + "분 "
    else:
        mtime = ""     

    strTime = dtime + htime + mtime + str(int(s)) + "초"    
    return strTime 

if __name__ == "__main__" :        
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()

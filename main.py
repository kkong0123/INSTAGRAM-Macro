from curses import KEY_ENTER
from random import randint
import random
from selenium import webdriver
import time
import sys
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def craw_main():
        global driver
        options = webdriver.ChromeOptions()
        # 창 숨기는 옵션 추가
        # options.add_argument("headless")
        if getattr(sys, 'frozen', False):
            chromedriver_path = os.path.join(sys._MEIPASS, "./chromedriver")
            driver = webdriver.Chrome(chromedriver_path, options=options)
        else:
            driver = webdriver.Chrome('./chromedriver',options=options)
            
        url = 'https://www.instagram.com/accounts/login/'
        driver.get(url)
        driver.implicitly_wait(15)

        login() #로그인 함수 호출
        search()
        # unfollow()

def login(): # 로그인 함수
    driver.find_element_by_css_selector(".-MzZI:nth-child(1) .zyHYP").send_keys("")
    time.sleep(random.uniform(2,5))
    driver.find_element_by_css_selector(".-MzZI+ .-MzZI .zyHYP").send_keys("")
    time.sleep(random.uniform(2,5))
    driver.find_element_by_css_selector(".-MzZI+ .DhRcB").click()
    driver.implicitly_wait(15)
    time.sleep(5)

def search():
    url = 'https://www.instagram.com/explore/tags/' + str("맞팔")
    driver.get(url)
    driver.implicitly_wait(15)
    time.sleep(5)

    pic_list = driver.find_elements_by_css_selector("._9AhH0")
    pic_list = list(pic_list)
    driver.implicitly_wait(15)
    time.sleep(5)
    pic_list[0].click()
    driver.implicitly_wait(15)
    time.sleep(5)

    # 인기게시물 건너뛰기
    for i in range(9):
        driver.find_element_by_css_selector(".l8mY4 .wpO6b").click()
        driver.implicitly_wait(15)
        time.sleep(5)

    for i in range(300):

        if (i+1) % 9 == 0: # 메크로 아닌척 (좋아요 - 댓글 - 팔로우 중간중간에 넣어야할듯)
            time.sleep(random.uniform(10,20))
            print("쉬어가기 {}".format(i+1))

        if (i+1) % 15 == 0:
            time.sleep(random.uniform(7,15))
            print("쉬어가기 {}".format(i+1))

        # 랜덤 메시지
        random_message = [
            "잘 보고갑니다! : )",
            "피드 잘 보고갑니다! :D",
            "피드 구경 잘 하고갑니다! : ) ",
            "게시물 잘보고갑니당! :)"
        ]
        random_message = random_message[randint(0,3)]

        driver.find_element_by_css_selector(".fr66n .wpO6b").click() # 좋아요 누르기
        print("{} Liked".format(i))
        time.sleep(random.uniform(3,6))

        try: # 댓글 남기기
            driver.find_element_by_css_selector(".X7cDz").click()
            time.sleep(random.uniform(1,5))
            driver.find_element_by_css_selector(".Ypffh").send_keys(random_message)
            time.sleep(random.uniform(1,5))
            driver.find_element_by_css_selector(".gtFbE").click()
            driver.implicitly_wait(15)
            time.sleep(random.uniform(4,6))
        except Exception:
            pass

        # 팔로우 하기
        try:
            driver.find_element_by_css_selector(".bY2yH .T0kll").click()
            time.sleep(random.uniform(7,12))
        except Exception:
            pass
        
        # 다음 버튼 누르기
        try:
            driver.find_element_by_css_selector(".l8mY4 .wpO6b").click()
            driver.implicitly_wait(30)
            time.sleep(random.uniform(3,6))
        except Exception:
            driver.find_element_by_css_selector(".l8mY4 .wpO6b").click()
            driver.implicitly_wait(10)
            time.sleep(random.uniform(2,6))

def unfollow():
    url = 'https://www.instagram.com/' + str("") 
    driver.get(url)
    time.sleep(3)
    driver.find_element_by_css_selector(".Y8-fY:nth-child(2) .g47SY").click()
    time.sleep(3)

    pop_up_window = WebDriverWait(
        driver, 2).until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='isgrP']")))
    
    # 팝업창 스크롤
    for i in range(20):
        driver.execute_script(
            'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', 
        pop_up_window)
        time.sleep(3)

    follower_list = []
    follower = driver.find_elements_by_css_selector("._0imsa .T0kll")

    for f in follower:
        follower_list.append(f.text)

    print(follower_list)
    print(len(follower_list))
    print('=='*20)
###########
    url = 'https://www.instagram.com/' + str("") 
    driver.get(url)
    time.sleep(3)
    driver.find_element_by_css_selector(".Y8-fY~ .Y8-fY+ .Y8-fY .g47SY").click()
    time.sleep(3)

    pop_up_window = WebDriverWait(
        driver, 2).until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='isgrP']")))
    
    # Scroll till Followers list is there
    for i in range(30):
        driver.execute_script(
            'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', 
        pop_up_window)
        time.sleep(1)

    following_list = []
    following = driver.find_elements_by_css_selector("._0imsa .T0kll")

    for f in following:
        following_list.append(f.text)

    print(following_list)
    print(len(following_list))
    print('=='*20)

    following_sub_follower = [x for x in following if x not in follower]
    print("맞팔 안됨")
    print(following_sub_follower)
    print(len(following_sub_follower))

craw_main()
from curses import KEY_ENTER
from random import randint
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
        time.sleep(1)

        login() #로그인 함수 호출
        # search()
        unfollow()


def login(): # 로그인 함수
    driver.find_element_by_css_selector(".-MzZI:nth-child(1) .zyHYP").send_keys("")
    time.sleep(randint(2,5))
    driver.find_element_by_css_selector(".-MzZI+ .-MzZI .zyHYP").send_keys("")
    time.sleep(randint(2,5))
    driver.find_element_by_css_selector(".-MzZI+ .DhRcB").click()
    time.sleep(10)

def search():
    url = 'https://www.instagram.com/explore/tags/' + str("작품")
    driver.get(url)
    time.sleep(5)

    pic_list = driver.find_elements_by_css_selector("._9AhH0")
    pic_list = list(pic_list)
    time.sleep(5)
    pic_list[0].click()
    time.sleep(5)

    for i in range(10):
        driver.find_element_by_css_selector(".fr66n .wpO6b").click()
        time.sleep(randint(3,6))
        print("{} : 하트".format(i))
        driver.find_element_by_css_selector(".l8mY4 .wpO6b").click()
        time.sleep(randint(3,6))

def unfollow():
    url = 'https://www.instagram.com/' + str("yu_an_0_0") 
    driver.get(url)
    time.sleep(3)
    driver.find_element_by_css_selector(".Y8-fY:nth-child(2) .g47SY").click()
    time.sleep(3)

    pop_up_window = WebDriverWait(
        driver, 2).until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='isgrP']")))
    
    # Scroll till Followers list is there
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
    url = 'https://www.instagram.com/' + str("yu_an_0_0") 
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
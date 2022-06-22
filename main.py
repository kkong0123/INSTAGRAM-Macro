from selenium import webdriver
from random import randint
import random
import time
import sys
import os

def craw_main():
        global instagram_id
        global instagram_pwd
        global search_tag
        global driver
        global start_time

##################################################

        instagram_id = ""
        instagram_pwd = ""
        search_tag = ""

##################################################

        start_time = time.time() # 시작시간
        options = webdriver.ChromeOptions()
        # options.add_argument("headless")

        if getattr(sys, 'frozen', False):
            chromedriver_path = os.path.join(sys._MEIPASS, "./chromedriver")
            driver = webdriver.Chrome(chromedriver_path, options=options)
        else:
            driver = webdriver.Chrome('./chromedriver',options=options)
            
        url = 'https://www.instagram.com/accounts/login/'   
        driver.get(url)
        driver.implicitly_wait(15)

        login() # 로그인 함수 호출
        # search() # 좋아요, 댓글, 팔로우 매크로 함수 호출
        # unfollow() # 언팔로우 매크로 함수 호출
        manual_unfollow()
def login(): # 로그인 함수
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

    for i in range(400):
        if (i+1) % 15 == 0: # 쉬어가기
            time.sleep(random.uniform(7,15))
            print('[' + time.strftime('%H:%M:%S') + ']' ,"쉬어가기, 누적 반복수: {}".format(i))

        try:
            # 랜덤 메시지
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
            follow_text = driver.find_element_by_css_selector("._aar2 ._aade").text

        except Exception: # 다음 계정 로딩 안되는 오류 발생할 때
                    time.sleep(random.uniform(3,6))
                    driver.find_element_by_css_selector("._aaqg ._abl-").click()
                    print('[' + time.strftime('%H:%M:%S') + ']' ,"로딩 오류 발생, 다음 게시물 이동 중..\n =======================================")
                    driver.implicitly_wait(30)   

                    #####
                    time.sleep(random.uniform(60,80))
                    #####

                     # 랜덤 메시지
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
                    follow_text = driver.find_element_by_css_selector("._aar2 ._aade").text


        if follow_text == "팔로우":

            #####
            time.sleep(random.uniform(60,80))
            #####

            # try:
            driver.find_element_by_css_selector("._aamw ._abl-").click() # 좋아요 누르기
            print('[' + time.strftime('%H:%M:%S') + ']' ,"{}번째 좋아요".format(i+1))
            time.sleep(random.uniform(3,6))
            # except Exception:
            #         driver.find_element_by_css_selector("._aaqg ._abl-").click()
            #         print('[' + time.strftime('%H:%M:%S') + ']' ,"로딩 오류 발생, 다음 게시물 이동 중..\n =======================================")
            #         driver.implicitly_wait(30)   # ._aaqg ._abl-
            #         time.sleep(random.uniform(3,6))

            #         #####
            #         time.sleep(random.uniform(60,80))
            #         #####

            #         driver.find_element_by_css_selector("._aamw ._abl-").click() # 좋아요 누르기
            #         print('[' + time.strftime('%H:%M:%S') + ']' ,"{}번째 좋아요".format(i+1))
            #         time.sleep(random.uniform(3,6))
            
            if (i+1) % 9 == 0: # 쉬어가기
                time.sleep(random.uniform(10,20))
                print('[' + time.strftime('%H:%M:%S') + ']' ,"쉬어가기, 누적 반복수: {}".format(i))

            try: # 댓글 남기기
                driver.find_element_by_css_selector("._aaoc").click()
                time.sleep(random.uniform(1,5))

                #####
                time.sleep(random.uniform(60,90))
                #####

                driver.find_element_by_css_selector("._aaoc").send_keys(random_message)
                time.sleep(random.uniform(1,5))

                ######
                time.sleep(random.uniform(60,80))
                ######

                driver.find_element_by_css_selector("._aad0").click()
                print('[' + time.strftime('%H:%M:%S') + ']' ,"{0}번째 댓글입력: {1}".format(i+1, random_message))
                driver.implicitly_wait(15)
                time.sleep(random.uniform(4,6))
            except Exception:
                pass

            # 팔로우 하기
            
            #####
            time.sleep(random.uniform(60,80))
            #####

            driver.find_element_by_css_selector("._aar2 ._aade").click()
            print('[' + time.strftime('%H:%M:%S') + ']' ,"{0}번째 팔로우".format(i+1))
            time.sleep(random.uniform(7,12))

            # 다음 버튼 누르기
            driver.find_element_by_css_selector("._aaqg ._abl-").click()
            print('[' + time.strftime('%H:%M:%S') + ']' ,"다음 게시물 이동 중..\n =======================================")
            print("======= 총 경과시간 =======")
            print(elapsedTime())
            driver.implicitly_wait(30)
            time.sleep(random.uniform(3,6))

        else:
            print('[' + time.strftime('%H:%M:%S') + ']' ,"[이미 팔로우한 유저입니다]\n{0}번째 작업 건너뛰기".format(i+1))
            time.sleep(random.uniform(3,6))
            driver.find_element_by_css_selector("._aaqg ._abl-").click()
            print('[' + time.strftime('%H:%M:%S') + ']' ,"다음 게시물 이동 중..\n =======================================")
            print("======= 총 경과시간 =======")
            print(elapsedTime())            
            driver.implicitly_wait(30)
            time.sleep(random.uniform(3,6))
            

def unfollow():
    # 팔로워 정보 수집
    url = 'https://www.instagram.com/' + instagram_id
    driver.get(url)
    time.sleep(3)
    driver.find_element_by_css_selector("._aa_5:nth-child(2) ._aade").click()
    time.sleep(3)

    scroll_box = driver.find_element_by_css_selector("._aano")

    last_ht, ht = 0, 1
    while last_ht != ht:
        last_ht = ht
        driver.implicitly_wait(30)
        time.sleep(4)            

        ht = driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight); 
            return arguments[0].scrollHeight;
            """, scroll_box)


    follower_list = []
    follower = driver.find_elements_by_css_selector("div > div > span > a > span")

    for f in follower:
        follower_list.append(f.text)

    print(follower_list)
    print(len(follower_list))
    print('=='*20)

    # 팔로잉 정보 수집
    url = 'https://www.instagram.com/' + instagram_id 
    driver.get(url)
    time.sleep(3)
    driver.find_element_by_css_selector("._aa_5~ ._aa_5+ ._aa_5 ._aade").click()
    time.sleep(3)

    # 팔로워 팝업창에서 아래까지 스크롤 다운하기
    scroll_box = driver.find_element_by_css_selector("._aano")
    last_ht, ht = 0, 1
    while last_ht != ht:
        last_ht = ht
        driver.implicitly_wait(30)
        time.sleep(5)

        ht = driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight); 
            return arguments[0].scrollHeight;
            """, scroll_box)

    following_list = []
    following = driver.find_elements_by_css_selector("div > div > span > a > span")

    for f in following:
        following_list.append(f.text)

    print(following_list)
    print(len(following_list))
    print('=='*20)

    following_sub_follower = [x for x in following_list if x not in follower_list]
    print("맞팔 안됨")

    print(following_sub_follower)
    print(len(following_sub_follower))
    print("======= 총 경과시간 =======")
    print(elapsedTime())

    n = 0
    # 맞팔 안된 사람 언팔하기
    for uf in following_sub_follower:
        url = 'https://www.instagram.com/' + str(uf) 
        driver.get(url)
        driver.implicitly_wait(30)
        try:
            #####
            time.sleep(random.uniform(120,160))
            #####

            n += 1
            time.sleep(random.uniform(10,30))
            driver.find_element_by_css_selector("._abni").click()
            time.sleep(random.uniform(10,30))

            #####
            time.sleep(random.uniform(120,160))
            #####

            driver.find_element_by_css_selector("._a9-_").click()
            print('[' + time.strftime('%H:%M:%S') + ']', "{0}/{1} 팔로우 취소 완료".format(n, len(following_sub_follower)))
            print("======= 총 경과시간 =======")
            print(elapsedTime())
            time.sleep(random.uniform(10,20))

            #####
            time.sleep(random.uniform(60,80))
            #####

        except Exception:
            ##### 매크로 경고 받았을 때 -> 오랫동안 대기
            time.sleep(random.uniform(600,900))
            #####
            pass

        
def manual_unfollow():
    following_sub_follower = ""
    n = 0
    # 맞팔 안된 사람 언팔하기
    for uf in following_sub_follower:
        url = 'https://www.instagram.com/' + str(uf) 
        driver.get(url)
        driver.implicitly_wait(30)
        try:
            #####
            time.sleep(random.uniform(120,160))
            #####

            n += 1
            time.sleep(random.uniform(10,30))
            driver.find_element_by_css_selector("._abni").click()
            time.sleep(random.uniform(10,30))

            #####
            time.sleep(random.uniform(120,160))
            #####

            driver.find_element_by_css_selector("._a9-_").click()
            print('[' + time.strftime('%H:%M:%S') + ']', "{0}/{1} 팔로우 취소 완료".format(n, len(following_sub_follower)))
            print("======= 총 경과시간 =======")
            print(elapsedTime())
            time.sleep(random.uniform(10,20))

            #####
            time.sleep(random.uniform(60,80))
            #####

        except Exception:
            ##### 매크로 경고 받았을 때 -> 오랫동안 대기
            time.sleep(random.uniform(600,900))
            #####
            pass


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


craw_main()
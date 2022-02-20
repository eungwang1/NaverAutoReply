#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import pyperclip
import random


# In[2]:


def clipboard_input(user_xpath, user_input):
        temp_user_input = pyperclip.paste()  # 사용자 클립보드를 따로 저장
        pyperclip.copy(user_input)
        driver.find_element(By.XPATH, user_xpath).click()
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

        pyperclip.copy(temp_user_input)  # 사용자 클립보드에 저장 된 내용을 다시 가져 옴
        time.sleep(1)
        
def login() :
    my_id = ent1.get()
    my_pw = ent2.get()
    driver.get(url)
    driver.implicitly_wait(5) # 로딩을 최대한 5초 정도 기다리겠다.
    driver.find_element(By.CSS_SELECTOR, '.link_login').click()
    driver.implicitly_wait(5)
    clipboard_input('//*[@id="id"]', my_id)
    driver.implicitly_wait(5)
    clipboard_input('//*[@id="pw"]', my_pw)
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//*[@id="log.login"]').click()
    
def tstoryLogin():
    tis_id = entTistoryID.get()
    tis_pw = entTistoryPW.get()
    driver.execute_script('window.open("about:blank", "_blank");')
    second_tab = driver.window_handles[1]
    driver.switch_to.window(window_name=second_tab)
    driver.get(tistory_url)
    driver.implicitly_wait(5)
    clipboard_input('//*[@id="id_email_2_label"]/span[1]', tis_id)
    clipboard_input('//*[@id="id_password_3_label"]/span[1]', tis_pw)
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//*[@id="login-form"]/fieldset/div[8]/button[1]').click()
    time.sleep(1)
    driver.close()
    first_tab = driver.window_handles[0]
    driver.switch_to.window(window_name=first_tab )
# 지식인 탭 이동
def MoveToKin():
    driver.get(kin_url)
    driver.implicitly_wait(5)
    
# 티스토리 이동
def MovetToBlog():
    # 새탭열기
    time.sleep(1)
    
    #driver.execute_script()를 이용하면 javascript를 실행할 수 있음.
    driver.execute_script('window.open("about:blank", "_blank");')
    second_tab = driver.window_handles[1]
    driver.switch_to.window(window_name=second_tab)
    driver.get(blog_url)
    driver.implicitly_wait(5)
    

# 티스토리 작업물 검색 후, 자료 복사
def TstorySearchingData():
    driver.find_element(By.XPATH, '//*[@id="mArticle"]/div/div[1]/form/div[2]/button[1]').click()
    time.sleep(1)
    action.send_keys(searchInput)
    time.sleep(1)
    action.send_keys(Keys.ENTER).perform()
    
    # 마우스오버후 , element가 나오면 클릭
    elem_hover = driver.find_element(By.XPATH, '//*[@id="mArticle"]/div/div[2]/ul/li[1]/div[2]')
    action.move_to_element(elem_hover).perform()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="mArticle"]/div/div[2]/ul/li/div[3]/div/div/a[1]').click()
    driver.implicitly_wait(5)
    ActionChains(driver).send_keys(Keys.TAB).key_down(Keys.CONTROL).send_keys('a').send_keys('c').key_up(Keys.CONTROL).perform()
    driver.close()
    first_tab = driver.window_handles[0]
    driver.switch_to.window(window_name=first_tab )
#     driver.find_element(By.XPATH, '//*[@id="tinymce"]').click()
#     time.sleep(1)
#     ActionChains(driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
    
    
    
# 랜덤으로 질문 선택    
def SelectQes():
    #자식요소 갯수 가져오기
    header =  driver.find_element(By.XPATH, '//*[@id="questionListTypePreview"]')
    questionLen = len(header.find_elements(By.CSS_SELECTOR,".answer_box._noanswerItem"))
    print(questionLen)
    randomIdx = random.randint(0,questionLen - 1)
    driver.find_elements(By.CSS_SELECTOR, '.tit_wrap')[randomIdx].click()
    # 현재탭 닫고 새탭으로 포커스 이동. 
    driver.close()   
    first_tab = driver.window_handles[0]
    driver.switch_to.window(window_name=first_tab )
    driver.implicitly_wait(5)
    time.sleep(2)
    action.send_keys(Keys.ENTER).perform()
    action.send_keys(Keys.ENTER).perform()
    time.sleep(2)

# 랜덤 키워드 생성
def createRandomInput():
    serchList =  ["게이밍노트북추천","게이밍키보드추천","게이밍모니터추천","액션캠추천","체중계추천"]
    randomSearchIdx = random.randint(0,len(serchList))
    global searchInput 
    searchInput = serchList[randomSearchIdx-1]
    
def NSearch():
    createRandomInput()
    MoveToKin()
    time.sleep(2)
    action.send_keys(Keys.ENTER).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="contentsOfMain"]').click()
    driver.find_element(By.XPATH, '//*[@id="main_content"]/div[2]/div[1]/div/div[2]/div[1]/div[1]/input').click()
    action.send_keys(searchInput)
    time.sleep(1)
    action.send_keys(Keys.ENTER).perform()
    time.sleep(2)
    SelectQes()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "se-container").click()
    MovetToBlog()
    TstorySearchingData()


def macroRun():
    try:
        global content_cnt
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "se-container").click()
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).send_keys(Keys.ENTER).perform()
        time.sleep(10)
        driver.find_element(By.XPATH, '//*[@id="answerRegisterButton"]/span').click()
    except:
        except_support()
    
def Repeat():
    repeat_num = int(ent4.get())    
    for i in range(repeat_num):
        time.sleep(10)
        macroRun()
        
        
def except_support():
    try:
        NSearch()
        macroRun()
    except:
        except_support()

    


# In[ ]:


win = Tk()
win.title("AutoReply")
win.geometry("800x800")
win.option_add("*Font", "나눔고딕 20")

driver = webdriver.Chrome()
url = "https://www.naver.com/"
blog_url = "https://gisastudy.tistory.com/manage/posts?category=-3&page=1&searchKeyword=&searchType=title&visibility=all"
kin_url = "https://kin.naver.com/"
tistory_url = 'https://accounts.kakao.com/login?continue=https%3A%2F%2Fkauth.kakao.com%2Foauth%2Fauthorize%3Fis_popup%3Dfalse%26ka%3Dsdk%252F1.41.0%2520os%252Fjavascript%2520sdk_type%252Fjavascript%2520lang%252Fko-KR%2520device%252FWin32%2520origin%252Fhttps%25253A%25252F%25252Fwww.tistory.com%26auth_tran_id%3Dv0gpfd33p58b8aef3eeb03fa312b81795386484f051kzl7h94m%26response_type%3Dcode%26state%3DaHR0cHM6Ly93d3cudGlzdG9yeS5jb20v%26redirect_uri%3Dhttps%253A%252F%252Fwww.tistory.com%252Fauth%252Fkakao%252Fredirect%26client_id%3Db8aef3eeb03fa312b81795386484f051'
action = ActionChains(driver)




# id 라벨
lab1 = Label(win)
lab1.config(text = "ID")
lab1.pack()

# id 입력창
ent1 = Entry(win)
ent1.pack()

# pw 라벨
lab2 = Label(win)
lab2.config(text = "Password")
lab2.pack()

# pw 입력창
ent2 = Entry(win)
ent2.pack()

# 로그인 버튼
btn1 = Button(win)
btn1.config(text="네이버 로그인")
btn1.config(command = login)
btn1.pack()

# TstroyId 라벨
labTistoryID = Label(win)
labTistoryID.config(text = "ID")
labTistoryID.pack()

# TstroyId 입력창
entTistoryID = Entry(win)
entTistoryID.pack()

# TstroyPw 라벨
labTistoryPW = Label(win)
labTistoryPW.config(text = "Password")
labTistoryPW.pack()

# TstroyPw 입력창
entTistoryPW = Entry(win)
entTistoryPW.pack()

# Tstroy 로그인 
btn7 = Button(win)
btn7.config(text="티스토리로그인")
btn7.config(command = tstoryLogin)
btn7.pack()


# # search 입력창
# ent3 = Entry(win)
# ent3.pack()

# 검색 버튼
btn2 = Button(win)
btn2.config(text="검색하기")
btn2.config(command = NSearch)
btn2.pack()


# 메시지 라벨
lab3 = Label(win)
lab3.pack()

# 1번 실행하기

btn5 = Button(win)
btn5.config(text="실행하기")
btn5.config(command = macroRun)
btn5.pack()


# 반복횟수 입력창
ent4 = Entry(win)
ent4.pack()

# 반복하기 클릭
btn6 = Button(win)
btn6.config(text="반복하기")
btn6.config(command = Repeat)
btn6.pack()




win.mainloop()


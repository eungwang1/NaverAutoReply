#!/usr/bin/env python
# coding: utf-8

# In[71]:


from tkinter import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
import pyperclip


# In[98]:


win = Tk()
win.title("Daum Log-in")
win.geometry("400x300")
win.option_add("*Font", "궁서 20")


driver = webdriver.Chrome()
url = "https://www.naver.com/"
blog_url = "https://blog.naver.com/tla1203"
action = ActionChains(driver)


# 로고
lab_d = Label(win)
img = PhotoImage(file = "C:/rabbit.png", master = win)

# img = img.subsample(2)  이미지 크기를 1/2로 줄인다
lab_d.config(image = img)
lab_d.pack()

# id 라벨
lab1 = Label(win)
lab1.config(text = "ID")
lab1.pack()

# id 입력창
ent1 = Entry(win)
ent1.insert(0,"temp@temp.com")  #0의 위치부터 글씨를 미리 넣는다.
def clear(event):
    if ent1.get() == "temp@temp.com":
        ent1.delete(0,len(ent1.get()))


ent1.bind("<Button-1>",clear)
ent1.pack()

#  pw 라벨
lab2 = Label(win)
lab2.config(text = "Password")
lab2.pack()

# pw 입력창
ent2 = Entry(win)
ent2.config(show = "*")
ent2.pack()

# 로그인 버튼
btn = Button(win)
btn.config(text="로그인")


def clipboard_input(user_xpath, user_input):
        temp_user_input = pyperclip.paste()  # 사용자 클립보드를 따로 저장
        pyperclip.copy(user_input)
        driver.find_element_by_xpath(user_xpath).click()
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

        pyperclip.copy(temp_user_input)  # 사용자 클립보드에 저장 된 내용을 다시 가져 옴
        time.sleep(1)
        
def login() :
    my_id = ent1.get()
    my_pw = ent2.get()
    driver.get(url)
    driver.implicitly_wait(5) # 로딩을 최대한 5초 정도 기다리겠다.
    driver.find_element_by_css_selector('.link_login').click()
    driver.implicitly_wait(5)
    clipboard_input('//*[@id="id"]', my_id)
    driver.implicitly_wait(5)
    clipboard_input('//*[@id="pw"]', my_pw)
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="log.login"]').click()
    lab3.config(text = "[메시지] 로그인성공")
btn.config(command = login)
btn.pack()

# 메시지 라벨
lab3 = Label(win)
lab3.pack()

win.mainloop()


# In[ ]:





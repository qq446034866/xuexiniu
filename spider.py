import re
import time
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from config import *

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)

""" 进入主页载入cookie"""
def index():
    try:
        browser.get('http://www.xuexiniu.com/')
        with open('cookies.txt', 'r') as f:
            cookies = list(eval(f.read()))

        for x in cookies:
            browser.add_cookie(x)

        index_page = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mn_forum > a')))
        index_page.click()
    except TimeoutException:
        return index

""" 存储cookie """
def get_cookies():
    time.sleep(20)
    cookies = browser.get_cookies()
    print(cookies)
    with open('cookies.txt', 'w') as f:
        f.write(str(cookies))

def click_menu():
    over = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#qmenu')))
    '''鼠标悬浮在menu'''
    if over:
        actions = ActionChains(browser)
        actions.move_to_element(over).perform()
        submit = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#qmenu_menu > ul > li:nth-child(5)')))
        time.sleep(1)
        browser.find_element_by_css_selector('#qmenu_menu > ul > li:nth-child(5)')
        submit.click()

    else:
        get_cookies()

def sign():
    try:
        browser.find_element_by_css_selector('#kx')

        kx = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#kx')))
        print(kx.value_of_css_property("border"))
        kx.click()
        if kx.value_of_css_property("border") == '2px dashed rgb(209, 216, 216)':
            web_input = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '#qiandao > table.tfm > tbody > tr:nth-child(1) > td > label:nth-child(3)')))
            web_input.click()
            onckick = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '#qiandao > table:nth-child(11) > tbody > tr > td > div > a > img')))
            onckick.click()
        print('签到成功')
    except:
        print('今天已经签到')
    finally:browser.close()



def main():
    index()
    # get_cookies()
    try:
        click_menu()
    except TimeoutException:
        print('登录信息已过去，请手动重新登录')
        get_cookies()
        return main()
    sign()

if __name__ == '__main__':
    main()
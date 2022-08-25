import time
import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
from plyer import notification


def send_message(contacts,msg):
    '''
    sending a pre written whatsapp message to a list of contacts
    :param contacts: a list of contacts - [(name1,phone1),...,(nameN,phoneN)]
    :param msg: the pre written message
    '''

    #connecting to whatsapp using selenium
    base_url = "https://web.whatsapp.com"
    driver_path = r"/usr/local/bin/chromedriver"
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument("user-data-dir=********") # can be found at chrome://version on chrome browser
    driver = webdriver.Chrome(executable_path=driver_path, options=driver_options)
    driver.minimize_window()
    driver.get(base_url)

    #sending the message to each contact
    for c_name, c_num in contacts:
        new_chat_btn = WebDriverWait(driver, 50).until(
            lambda driver: driver.find_element(By.XPATH, "//div[@title='New chat']"))
        new_chat_btn.click()

        search_box = WebDriverWait(driver, 50).until(
            lambda driver: driver.find_element(By.XPATH,"//div[@title='Search input textbox']"))
        search_box.send_keys(c_num + Keys.ENTER)

        msg_box = WebDriverWait(driver, 50).until(
            lambda driver: driver.find_element(By.XPATH, "//div[@title='Type a message']"))
        msg_box.send_keys("Hello " + c_name + " ," + msg + Keys.ENTER)
        time.sleep(1)
    #waiting before closing the webdriver in order to be sure that the messages were sent
    time.sleep(5)
    driver.quit()

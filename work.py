from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

import pandas as pd
from time import sleep
import string  # for string constants
import random  # for generating random strings
import time
import email
import imaplib
import smtplib


TARGET_URL = "https://app.arbitool.eu/login"
USERNAME = 'Modo'
PASSWORD = 'iraqIRAQ@1'






# Main Function
def main():

    buyList = []
    buyArray = []
    atExchangeArray = []
    forArray = []
    sellAtArray = []
    nextForArray = []
    transferTimeArray = []
    profitArray = []
    maxValueArray = []
    maxValueUSDArray = []
    atExchangeList = []
    forList = []
    sellAtList = []
    nextForList = []
    transferTimeList = []
    profitList = []
    maxValueList = []
    maxValueUSDList = []
    # Run Chrome Driver
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1200, 800)
    driver.get(TARGET_URL)
    # login to site
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "username"))).send_keys(USERNAME)
        print("User name inputed!!!")
    except TimeoutException:
        print ("Loading took too much time!")
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "password"))).send_keys(PASSWORD)
        print("User Password inputed!!!")
    except TimeoutException:
        print ("Loading took too much time!")
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "button"))).click()
        print("Login Button is clicked!!!")
    except TimeoutException:
        print ("Login Button was not clicked!")
    # buyArray = driver.find_elements_by_xpath("//table[@id='table-1']/tbody/tr/td[1]")
    time.sleep(3)
    try:
        print(EC.element_to_be_clickable((By.XPATH, "//div[@class='multiselect__clear'][1]")))
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='multiselect__clear'][1]"))).click()
        print("clear selected")
    except TimeoutException:
        print ("Loading took too much time!")
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='multiselect__select'][1]"))).click()
        print("clear selected")
    except TimeoutException:
        print ("Loading took too much time!")
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='multiselect__content'][1]/li[1]"))).click()
        print("clear selected")
    except TimeoutException:
        print ("Loading took too much time!")
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='multiselect__content'][1]/li[6]"))).click()
        print("clear selected")
    except TimeoutException:
        print ("Loading took too much time!")
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='multiselect__content'][1]/li[8]"))).click()
        print("clear selected")
    except TimeoutException:
        print ("Loading took too much time!")
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='multiselect__content'][1]/li[11]"))).click()
        print("clear selected")
    except TimeoutException:
        print ("Loading took too much time!")
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='multiselect__content'][1]/li[14]"))).click()
        print("clear selected")
    except TimeoutException:
        print ("Loading took too much time!")
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='multiselect__content'][1]/li[15]"))).click()
        print("clear selected")
    except TimeoutException:
        print ("Loading took too much time!")
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='multiselect__select'][1]"))).click()
        print("clear selected")
    except TimeoutException:
        print ("Loading took too much time!")





    # From Exchange selected






    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='searchBar']/div[1]/div[2]/div[2]/div[2]"))).click()
        print("selected")
    except TimeoutException:
        print ("1")
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='searchBar']/div[1]/div[2]/div[2]/div[1]"))).click()
        print("selected")
    except TimeoutException:
        print ("2")
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='searchBar']/div[1]/div[2]/div[2]/div[4]/ul/li[1]"))).click()
        print("selected")
    except TimeoutException:
        print ("3")
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='searchBar']/div[1]/div[2]/div[2]/div[4]/ul/li[6]"))).click()
        print("selected")
    except TimeoutException:
        print ("4")
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='searchBar']/div[1]/div[2]/div[2]/div[4]/ul/li[8]"))).click()
        print("selected")
    except TimeoutException:
        print ("5")
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='searchBar']/div[1]/div[2]/div[2]/div[4]/ul/li[11]"))).click()
        print("selected")
    except TimeoutException:
        print ("6")
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='searchBar']/div[1]/div[2]/div[2]/div[4]/ul/li[14]"))).click()
        print("selected")
    except TimeoutException:
        print ("7")
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='searchBar']/div[1]/div[2]/div[2]/div[4]/ul/li[15]"))).click()
        print("clear selected")
    except TimeoutException:
        print ("8")
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='searchBar']/div[1]/div[2]/div[2]/div[1]"))).click()
        print("clear selected")
    except TimeoutException:
        print ("9")
    buyArray = driver.find_elements(by=By.XPATH, value="//table[@id='table-1']/tbody/tr/td[1]")
    atExchangeArray = driver.find_elements(by=By.XPATH, value="//table[@id='table-1']/tbody/tr/td[2]")
    forArray = driver.find_elements(by=By.XPATH, value="//table[@id='table-1']/tbody/tr/td[3]")
    sellAtArray = driver.find_elements(by=By.XPATH, value="//table[@id='table-1']/tbody/tr/td[5]")
    nextForArray = driver.find_elements(by=By.XPATH, value="//table[@id='table-1']/tbody/tr/td[6]")
    transferTimeArray = driver.find_elements(by=By.XPATH, value="//table[@id='table-1']/tbody/tr/td[7]")
    profitArray = driver.find_elements(by=By.XPATH, value="//table[@id='table-1']/tbody/tr/td[8]")
    maxValueArray = driver.find_elements(by=By.XPATH, value="//table[@id='table-1']/tbody/tr/td[9]")
    maxValueUSDArray = driver.find_elements(by=By.XPATH, value="//table[@id='table-1']/tbody/tr/td[10]")
    
    try:
        for i in range(len(buyArray)):
            buyList_ele = ''
            atExchangeList_ele = ''
            forList_ele = ''
            sellAtList_ele = ''
            nextForList_ele = ''
            transferTimeList_ele = ''
            profitList_ele = ''
            maxValueList_ele = ''
            maxValueUSDList_ele = ''
            try:
                buyList_ele = buyArray[i].text
                atExchangeList_ele = atExchangeArray[i].text
                forList_ele = forArray[i].text
                sellAtList_ele = sellAtArray[i].text
                nextForList_ele = nextForArray[i].text
                transferTimeList_ele = transferTimeArray[i].text
                profitList_ele = profitArray[i].text
                maxValueList_ele = maxValueArray[i].text
                maxValueUSDList_ele = maxValueUSDArray[i].text
            except:
                print('OK')
            finally:
                if(buyList_ele or atExchangeList_ele or forList_ele or sellAtList_ele or nextForList_ele or transferTimeList_ele or profitList_ele or maxValueList_ele or maxValueUSDList_ele):
                    buyList.append(buyList_ele)
                    atExchangeList.append(atExchangeList_ele)
                    forList.append(forList_ele)
                    sellAtList.append(sellAtList_ele)
                    nextForList.append(nextForList_ele)
                    transferTimeList.append(transferTimeList_ele)
                    profitList.append(profitList_ele)
                    maxValueList.append(maxValueList_ele)
                    maxValueUSDList.append(maxValueUSDList_ele)
    except:
        print ("Error is now!!!")
    print(len(buyList),len(atExchangeList),len(forList),len(sellAtList),len(forList),len(transferTimeList),len(profitList),len(maxValueList),len(maxValueUSDList))
    data = {
        'Buy':buyList,
        'at exchange':atExchangeList,
        'for':forList,
        'Sell at':sellAtList,
        'for':forList,
        'Transfer Time':transferTimeList,
        'profit':profitList,
        'Max value':maxValueList,
        'Max value USD':maxValueUSDList
    }

    result = pd.DataFrame(data,columns=['Buy','at exchange','for','Sell at','for','Transfer Time','profit','Max value','Max value USD'])
    # result.to_csv('result.csv', mode='w')
    gmail_user = 'fofislav@gmail.com'
    gmail_password = '809'

    sent_from = gmail_user
    to = ['promisi@gmail.com', 'sh.03@gmail.com']
    subject = 'Updating Data'
    body = str(result)

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sent_from, to, email_text)
        smtp_server.close()
        print ("Email sent successfully!")
    except Exception as ex:
        print ("Something went wrong….",ex)
    driver.quit()
main();
while True:
    main();
    time.sleep(60)




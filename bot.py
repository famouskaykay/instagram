from selenium import webdriver
import time
import random
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class bot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome("chromedriver.exe")
        
    def login(self):
        print('login initiated')
        chrome_browser = self.driver
        chrome_browser.implicitly_wait(3)
        chrome_browser.get('https://www.instagram.com/')
        
        time.sleep(5)
        

        username_input = chrome_browser.find_element_by_xpath("//input[@name='username']")
        chrome_browser.implicitly_wait(5)
        password_input =chrome_browser.find_element_by_xpath("//input[@name='password']")
        chrome_browser.implicitly_wait(5)
        username_input.clear()
        chrome_browser.implicitly_wait(5)
        password_input.clear()
        chrome_browser.implicitly_wait(5)
        
        username_input.send_keys(self.username)
        chrome_browser.implicitly_wait(5)
        password_input.send_keys(self.password)
        chrome_browser.implicitly_wait(5)

        login_button = chrome_browser.find_element_by_tag_name('form')
        login_button.submit()
        chrome_browser.implicitly_wait(10)
        
        
        print('login complete')
        time.sleep(10)
    
    def searchHashtag(self,hashtag) :
        print('serching initiated')
        chrome_browser = self.driver
        chrome_browser.implicitly_wait(3)
        chrome_browser.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        print('searching finish')
        time.sleep(5)
        
    
    def likePhoto(self,amount):
        chrome_browser = self.driver
        print('opening photo')
        chrome_browser.implicitly_wait(3)
        chrome_browser.find_element_by_class_name('_9AhH0').click()
        time.sleep(2)
        
        
        i=1
        while i<=amount:
            print('likiing started')
            try:
                chrome_browser.find_element_by_css_selector('svg[aria-label="Like"]').click()
            except:
                pass
            print('liked')
            print(i)
            time.sleep(2)
            
            print('next image')
            try:
                chrome_browser.find_element_by_xpath('//a[contains(text(),"Next")]').click()
            except:
                chrome_browser.get('https://www.instagram.com/'+self.username)
            time.sleep(3)
            i+=1
        chrome_browser.get('https://www.instagram.com/'+self.username)
            
    
    def securityCheck(self):
        chrome_browser = self.driver
        
        
        chrome_browser.implicitly_wait(3)
        print('checking for two step verification')
        try:
            check_str=chrome_browser.find_element_by_id('verificationCodeDescription').text
        except:
                return False
            
        sample_str='Enter the code we sent'
        if sample_str in check_str:
            return True
        else:
            return False
        
        print('checked for two step verification ')
    
    def setCode(self,code):
        chrome_browser = self.driver
        chrome_browser.implicitly_wait(3)
        print('seting up code given by usser')
        securityCode=chrome_browser.find_element_by_xpath('//input[@aria-label="Security Code"]')
        securityCode.clear()
        securityCode.send_keys(code)
        time.sleep(2)
        confirm=chrome_browser.find_element_by_xpath('//button[contains(text(),"Confirm")]')
        confirm.click()
        print('code verification done')
        
    def closeBrowser(self):
        self.driver.close()
        
   
insta=bot('USERNAME','PASSWORD')
insta.login()
i=1
while True:
    
    if insta.securityCheck():
        if i>1:
            print('!!!!!!opps pls enter correct code!!!!!!!!!')
        print('pls enter code recived in your phone---')
        code=input()
        insta.setCode(code)
        
        i+=1
    else:
        break
    time.sleep(15)


username = os.environ.get("username")
password = os.environ.get("password")

insta.searchHashtag('gainwithmchina')
insta.likePhoto(100)
insta.closeBrowser()       
        
        

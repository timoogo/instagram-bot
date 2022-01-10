from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from time import sleep
import _secret

class InstagramBot:
    def __init__(self, username, password):
        self.username = _secret._username
        self.password = _secret._password
        self.bot      = webdriver.Chrome(executable_path=_secret._driverPath)
    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login')
        bot.find_element(By.XPATH,'/html/body/div[4]/div/div/button[1]').click()
        sleep(1)
        bot.find_element(By.NAME,'username').send_keys(self.username)
        bot.find_element(By.NAME,'password').send_keys(self.password + Keys.RETURN)
        sleep(8)
        
        bot.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/button')\
        .click()
        print('yo')
        sleep(20)
        bot.find_element(By.CLASS_NAME, "aOOlW")\
        .click()

    def searchHashtag(self, hashtag):
        bot = self.bot
        bot.get('https://www.instagram.com/explore/tags/' + hashtag)
    def searchUsername(self, _usernameToFind):
        bot = self.bot
        bot.get('https://www.instagram.com/' + _usernameToFind)
    def likePhotos(self, amount):
        bot = self.bot
        bot.find_element(By.CLASS_NAME,'v1Nh3').click()
        i = 0 
        while i < amount:
            sleep(1)
            bot.find_element(By.CLASS_NAME,'fr66n').click()
            bot.find_element(By.CLASS_NAME,'l8mY4').click()
            i += 1
        bot.get('https://www.instagram.com/' + self._username)
   


insta = InstagramBot(_secret._username, _secret._password)
insta.login()
#insta.searchUsername("frenchcoder")
insta.searchHashtag('python')
insta.likePhotos(3) 


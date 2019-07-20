from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random


class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def close_browser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(2)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        password_elem = driver.find_element_by_xpath("//input[@name='password']")
        password_elem.clear()
        password_elem.send_keys(self.password)
        password_elem.send_keys(Keys.ENTER)
        time.sleep(2)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='aOOlW   HoLwm ']"))).click()

    def like_photo(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)
        for i in range(1, 8):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        pic_hrefs = [href for href in pic_hrefs]
        count_comment = 0
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            try:
                driver.find_element_by_xpath("//span[@class='fr66n']").click()
                count_comment += 1
                if count_comment == 30:
                    count_comment = 0
                    text_box = driver.find_element_by_class_name('Ypffh')
                    text_box.click()
                    text_box = driver.find_element_by_class_name('Ypffh')
                    comments = ['Wow, that is amazing...', 'OMG, so cool!', 'Cool post!', 'This is amazing... follow me!', ':) cool picture, it captures everything!']
                    comment_index = []
                    rand = random.randrange(0, len(comments))
                    comment_index.append(rand)
                    while rand in comment_index:
                        if rand+1 < len(comments):
                            rand += 1
                            break
                        else:
                            if rand-1 >= 0:
                                rand -= 1
                                break
                    else:
                        continue
                    text_box.send_keys(comments[rand])
                    text_box.send_keys(Keys.ENTER)
                else:
                    time.sleep(18)
            except Exception as e:
                print(e.args)
                time.sleep(2)

    def like_following_posts(self):
        driver = self.driver
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//span[@class='fr66n']")))
            like_photos = driver.find_elements_by_xpath("//span[@class='fr66n']")
            for photo in like_photos:
                try:
                    photo.click()
                    time.sleep(18)
                except Exception as e:
                    print(e.args)
                    time.sleep(2)
            time.sleep(2)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    def follow(self):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/people/suggested/")
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            people_to_follow = driver.find_elements_by_xpath("//button[@class='_0mzm- sqdOP  L3NKy ']")
            for person in people_to_follow:
                try:
                    person.click()
                    time.sleep(18)
                except Exception as e:
                    print(e.args)
                    time.sleep(2)
            time.sleep(2)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    def user_info(self, user):
        driver = self.driver
        driver.get("https://www.instagram.com/" + user + "/")
        information = driver.find_elements_by_xpath("//span[@class='g47SY ']")
        word_list = ['posts', 'followers', 'following']
        count_wl = 0
        for each_info in information:
            print(word_list[count_wl], "= ", each_info.get_attribute('innerHTML'))
            count_wl += 1

    def like_user_pics(self, user):
        pass


file = open("M:\cred.txt", "r")
username = file.readline()
password = file.readline()

myIg = InstagramBot(username, password)
myIg.login()
file.close()
# [myIg.user_info(user) for user in users]
# myIg.follow()
# hashtags = ['apexlegends', 'college']
# [myIg.like_photo(tag) for tag in hashtags]
# myIg.like_following_posts()

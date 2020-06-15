#secrets file has username and password.
#In the format 
#username="djbdsnsdns"
# password="dvjndsjvnd"


from selenium import webdriver
from time import sleep
from secrets import username,password
from selenium.webdriver.common.keys import Keys

class Instabot :
    def __init__(self,uname,pw):
        self.uname = uname
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.instagram.com/")
        sleep(2)

        #logging_in
        self.logging_function(self.driver.find_element_by_xpath("//input[@name=\"username\"]"),self.driver.find_element_by_xpath("//input[@name=\"password\"]"),uname,pw)
        sleep(3)
        self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
        sleep(3)
        self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()

    def logging_function(self,d1,d2,uname,pw):
        #Entering Uname
        for character in uname :
            d1.send_keys(character)
            #sleep(0.3)
        #Entering password
        for character in pw :
            d2.send_keys(character)
            #sleep(0.3)
        #clicking login
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()


    def get_unfollowers(self):
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a').click()
        sleep(2)

        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
        sleep(2)
        followers = self._get_names()
        print("Followers - ",followers)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
        following = self._get_names()
        print("Following - ",following)
        not_following_back = [user for user in following if user not in followers]
        print("Not Following Back - ",not_following_back)


    def _get_names(self):
        sleep(2)
        scroll_box = self.driver.find_element_by_xpath('//html/body/div[4]/div/div')

        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                        arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                        return arguments[0].scrollHeight;
                        """, scroll_box)

        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/div[2]/button').click()
        #print(names)
        return names[2:]


bot = Instabot(username,password)
sleep(2)
bot.get_unfollowers()

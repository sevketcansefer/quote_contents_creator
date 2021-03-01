from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime
import os

class ImageFinder():
    
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:/Python_Files/chromedriver.exe')
        

    def get_content_img(self,category,picAmount):
        """
        Creates category direction and downloads images via web scrapping related with the category given as an argument.
        """

        self.category = category
        self.picAmount = int(picAmount)

        # https://unsplash.com/ a website that have CC Licenced photos
        self.driver.get("https://unsplash.com/")
        searchInput = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[1]/div/div[2]/div[1]/div/div/div/div/div[1]/form/div[1]/input')

        searchInput.send_keys(self.category)
        searchInput.send_keys(Keys.ENTER)
        time.sleep(1)

        soup = BeautifulSoup(self.driver.page_source, "html.parser")

        img_tags = soup.find_all("img", "_2UpQX")
        
        # Creating and checking directories
        self.cwd = str(os.getcwd())
        os.chdir(self.cwd + "/mood_pics")
        
        if not os.path.exists(self.cwd + f"/mood_pics/{self.category}" ):
            os.mkdir(f"{self.category}")
            os.chdir(self.cwd + f"/mood_pics/{self.category}")
        else:
            os.chdir(self.cwd + f"/mood_pics/{self.category}")
        
        # Saving images
        imgCount = 0
        try:
            print("Download Starting...")
            for i in range(self.picAmount):
                try:
                    self.imageName = str(img_tags[i]["alt"]).replace(" ","_")
                except:
                    self.imageName = str(self.category) + str(i) + ".jpeg"

                urllib.request.urlretrieve(img_tags[i]['src'], str(self.imageName) + str(i) + ".jpeg")
                imgCount += 1
            os.chdir(self.cwd)
        except Exception as e:
            print(f"Downloaded {imgCount} {self.category} Background Pictures images instead of {self.picAmount}. Error: {e}")
            if imgCount == 0:
                os.remove(self.cwd + f"/mood_pics/{self.category}")
            os.chdir(self.cwd)









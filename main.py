import json
import random
from img_finder import ImageFinder
from img_manipulator import ImageCreator
import pandas as pd


"""
    # I get data (quotes.json) form kaggle.com  
    # Lot of Quote was reccurring, created new file which one Quote appears once. 

unique = { each['Quote'] : each for each in data }.values()

with open("quotes.json", "w") as write_file:
    json.dump(data, write_file)
"""

class QuoteApp():

    def __init__(self):
        # open and load json file
        self.preData = open("quotes.json", encoding="UTF-8")
        self.data = json.load(self.preData)
        # create category list without recur
        self.categorySet = set()
        for i in range(len(self.data)):
            self.categorySet.add(self.data[i]["Category"])

        self.categoryList = list(self.categorySet)
        self.categoryList.remove("")
        # Creating pandas DataFrame
        pandasData = pd.read_json("quotes.json")
        dataFrame = pd.DataFrame(pandasData)
        
        self.desiredCategory = str(input("Please input the desired category:")).strip().lower()
        categorizedQuotes = dataFrame[dataFrame["Category"] == self.desiredCategory]
        self.quote = random.choice(list(categorizedQuotes["Quote"]))

    def content_downloader(self):
        """
        Creates photo library that will be used to create contents.
        """
        self.image_finder = ImageFinder()
        # This structure will try to download 10 photos for each category. It can be changed easily for download only desired category.
        for category in self.categoryList:
            self.image_finder.get_content_img(str(category),10)
        self.image_finder.driver.close()
    
    def get_image(self):
        self.image_creator = ImageCreator(self.desiredCategory,self.quote)
        self.image_creator.text_writer() 


x = QuoteApp()
x.get_image()
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
import random
import textwrap
import cv2
import numpy as np
import datetime

class ImageCreator():

    def __init__(self,category,quote):
        self.category = category
        self.quote = quote

    def image_cutter(self):
        """
        Cuts and creates square image from random image inside the direction that given as category. 
        """
        
        self.cwd = os.getcwd()
        self.direction = self.cwd + "/mood_pics" +f"/{self.category}" 
        self.listOfImages = os.listdir(self.direction)
        
        while True:
            self.randomImageName = random.choice(self.listOfImages)
            try:
                    
                self.img = Image.open(self.direction + f"/{self.randomImageName}")
                self.x, self.y = self.img.size
                
                # making the picture square:
                if self.x > self.y :
                    delta = self.x - self.y
                    
                    left,upper,right,lower = int(delta/2), 0, (self.x  - int(delta/2)) , self.y
                    
                    cropped = self.img.crop((left,upper,right,lower))
                    
                elif self.y > self.x :
                    delta = self.y - self.x
                    
                    left,upper,right,lower = 0, int(delta/2), self.x,  (self.y - int(delta/2)) 

                    cropped = self.img.crop((left,upper,right,lower))
                    
                return cropped
                
                
            except Exception as e:
                print("Cutting process went wrong :" ,e)
                continue
    
    def image_filter(self):
        self.img = self.image_cutter()
        #self.img = Image.open("test.png")
        filteredImage = self.img.filter(ImageFilter.GaussianBlur(radius= 3))
        
        return filteredImage
    
    def darknes_finder(self,image):
        # Thanks to kmohrf for brightness.py on github
        self.image = image
        greyscale_img = self.image.convert("L")
        histogram = greyscale_img.histogram()
        pixels = sum(histogram)
        brightness = scale = len(histogram)
        for index in range(0,scale):
            ratio = histogram[index] / pixels
            brightness += ratio * (-scale + index)

        return 1 if brightness == 255 else brightness / scale

    def text_writer(self):
        textt = self.quote
        my_img = self.image_filter()
        
        imgDraw = ImageDraw.Draw(my_img)
        imgWidth, imgHeight = my_img.size
        
        fontDictionary = {
            "Direct.ttf": ["arts","books","education","knowledge","mind","philosophy","poetry"],
            "Serious.ttf": ["death","faith","god","purpose","religion","truth","wisdom"],
            "Try.otf": ["friendship","funny","happiness","hope","humor","inspiration","mind"],
            "Love.otf": ["love","life","romance","quotes","science","writing","motivation","positive","relationship"]

        }
        for key,value in fontDictionary.items():
            if self.category in value:
                fontName = key

        if fontName == "Love.otf":
            fontSize = imgWidth // 10
        elif fontName == "Serious.ttf":
            fontSize = imgWidth // 17
        else:
            fontSize = imgWidth // 15
        
        fontDir = self.cwd + f"/fonts/{fontName}" 
        font = ImageFont.truetype(fontDir,fontSize)

        lines = textwrap.wrap(textt, width=30)
        height = font.getsize(lines[0])[1]
        totalHeightPx = len(lines) * height 
        textStartY = (imgHeight - totalHeightPx) / 2

        self.brightnessLevel = self.darknes_finder(my_img)
        if self.brightnessLevel < 0.50:
            fontColor = (230, 230, 230,200)
            strokeColor = (55, 55, 55)
        elif  0.50 <= self.brightnessLevel  < 0.75:
            fontColor = (72, 72, 72, 200)
            strokeColor = (230, 230, 230,200)
        else:
            fontColor = (55, 55, 55, 200)
            strokeColor = (230, 230, 230,200)
        
        for line in lines:
            width = font.getsize(line)[0]   
            imgDraw.text(((imgWidth-width)/2,textStartY), line,font=font, fill = fontColor, stroke_width= 2, stroke_fill= strokeColor)
            textStartY += height


        now = datetime.datetime.now()
        self.timeStamp = str(now.strftime("%d/%m/%Y")).replace("/","_")
        savingName = f"{self.timeStamp}_{self.category}.png"
        my_img.save(f"{self.cwd}/created_contents/{savingName}")
        
        
        

        



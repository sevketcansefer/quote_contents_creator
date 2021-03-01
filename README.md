# quote_contents_creator
This project is basic python training that aims create instagram quote contents easily.

# Creating square images that has centered quotes
  Quotes are one of the most viewed instagram/facebook contents according to [here](http://blog.marginmedia.com.au/our-blog/instagram-9-types-of-content-that-get-the-most-engagement). In this piece of code I've challenged myself to solve some problems while using few of the most popular libraries of python. Aim of the code is having one word input from user (category of quote) and at the end saving square shaped image which has random quote text content with related background.   
  
  #### main.py reaches 2 main class:
  
  1- Main block firstly opens json file which I obtained on: [Quotes-Dataset](https://www.kaggle.com/akmittal/quotes-dataset). Creates pandas DataFrame and QuoteApp class takes one argument: desired category. From this DataFrame chooses randomly quote and sends this two argument to the img_manipulator.py, ImageCreator class.
   
   
   1.1- img_finder.py -> ImageFinder class:
        - Based on bs4 and selenium libraries. It has function that uses chrome webdriver to reach unsplash.com to search and download images that will be used as background images for contents. Automaticly creates directories under /mood_pics folder with the names of categories.
    
   1.2- img_manipulator.py -> ImageCreator class:
        - Based on PIL,cv2 libraries. It has series of functions works for 1: Image cutting function returns square image, 2: Image Filter function, 3: Darkness Finder function in order to determine color of the text, 4: Text writer function that does calculations and writes the text on image.

#### *This project is not intended for commercial purposes. I strongly suggest that legal research should have done (for json file, webscrapping from unsplash.com and using fonts) if you would like to copy and use it with purposes other than educational or self use.*


## Some contents created by this creator:

### Love argument given:
![Content-1](https://github.com/sevketcansefer/quote_contents_creator/blob/main/created_contents/01_03_2021_love.png "Love Category Content")

### Relationship argument given:
![Content-2](https://github.com/sevketcansefer/quote_contents_creator/blob/main/created_contents/01_03_2021_relationship.png "Relationship Category Content")

### Religion argument given:
![Content-3](https://github.com/sevketcansefer/quote_contents_creator/blob/main/created_contents/01_03_2021_religion.png "Religion Category Content")

### Poetry argument given:
![Content-4](https://github.com/sevketcansefer/quote_contents_creator/blob/main/created_contents/01_03_2021_poetry.png "Poetry Category Content")

### God argument given:
![Content-5](https://github.com/sevketcansefer/quote_contents_creator/blob/main/created_contents/01_03_2021_god.png "God Category Content")



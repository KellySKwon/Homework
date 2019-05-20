# Dependencies
import requests
from bs4 import BeautifulSoup as bs
from splinter import Browser
import pymongo
import os
import pandas as pd


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)



def scrape():
    browser = init_browser()

    # Create dictionary to hold info
    listings = {}
    
    """NEWS"""
    # URL of page to be scraped
    newsUrl = "https://mars.nasa.gov/news/"
    browser.visit(newsUrl)

    # Create BeautifulSoup object; parse with 'html'
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')

    # Retrieve elements to collect the latest News Title
    news_title = soup.find('div', class_='content_title').text

    # Retrieve elements to collect the Paragraph
    news_p = soup.find('div', class_='article_teaser_body').text

    # Store in dictionary

    listings['newsTitle'] = news_title
    listings['newsTeaser'] = news_p

    """JPL Mars Space Images"""

    # JPL Images
    jplUrl = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars/'
    browser.visit(jplUrl)

    # HTML object
    html = browser.html

    # Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')

    # Retrieve Mar's featured image
    jplImage = soup.find('article',class_='carousel_item')['style']

    # Split text to get url
    imageString = jplImage.split("'",2)
    imageURL = imageString[1]

    # Create URL for Image
    featured_image_url = 'https://www.jpl.nasa.gov' + imageURL

    # Store in dictionary

    listings['featuredImage'] = featured_image_url


    """MARS Twitter"""

    # URL of page to be scraped
    TwitterUrl = "https://twitter.com/marswxreport?lang=en"

    browser.visit(TwitterUrl)
    
    # Create BeautifulSoup object; parse with 'html'
    html = browser.html
    
    # Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')
    
    # Retrieve elements to collect the latest weather tweet
    mars_weather = soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text

    # Store in dictionary

    listings['tweet'] = mars_weather


    """MARS Facts"""
    # Use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

    # URL of table to be scraped
    factUrl = "https://space-facts.com/mars/"
    
    # Use read html to read table 
    tables = pd.read_html(factUrl)

    # There's only one table so use normal indexing to get first dataframe
    df = tables[0]
    df.columns = ['Attribute','Metrics']
    df = df.set_index('Attribute')

    # Generate HTML tables from DataFrames
    html_table = df.to_html()

    # Strip unwanted newlines to clean up the table.
    cleanTable = html_table.replace('\n', '')

    # Store in dictionary

    listings['table'] = cleanTable

    """MARS Hemisphere"""

    """
        Separate Links for Full Images of Hemispheres:

        https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced
        https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced
        https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced
        https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced

    """

    hemList = ['cerberus_enhanced','schiaparelli_enhanced','syrtis_major_enhanced','valles_marineris_enhanced']
    imgList = []

    for i in hemList:
        # URL of Image to be scraped
        ImageUrl = "https://astrogeology.usgs.gov/search/map/Mars/Viking/" + i
        browser.visit(ImageUrl)

        # Create BeautifulSoup object; parse with 'html'
        html = browser.html

        # Parse HTML with Beautiful Soup

        soup = bs(html, 'html.parser')
        # Find Items

        # Find Image
        image = soup.find('img', class_='wide-image')['src']
        imgString = "https://astrogeology.usgs.gov" + image
        
        # Append to list
        imgList.append(imgString)

    # URL of Titles to be scraped
    titleUrl = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(titleUrl)

    # Create BeautifulSoup object; parse with 'html'
    html = browser.html

    # Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')

    # Find hemispheres
    hemispheres = soup.find_all('div',class_='item')

    titleList = []

    for each in hemispheres:
        image = each.find('a', class_='itemLink product-item')['href']
        imageURL = "https://astrogeology.usgs.gov" + image
            
        title = each.find('h3').text
        titleList.append(title)

        hemi_dict = []

    for i in range(0,4):
        hemi_dict.append({'title':titleList[i],'img_url':imgList[i]})

    
    # Store in dictionary

    listings['hemURLs'] = hemi_dict


    # Close the browser after scraping
    browser.quit()

    # Return results
    return listings
#!/usr/bin/env python
# coding: utf-8

# In[25]:


from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd


# In[26]:


# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': 'C:/Users/Documents/chromedriver'}
browser = Browser('chrome', executable_path)


# In[27]:


###Visit the NASA mars news site


# In[28]:


# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


# In[29]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('ul.item_list li.slide')


# In[30]:


slide_elem.find("div", class_='content_title') 


# In[31]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title


# In[32]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p


# In[33]:


###JPL Space Images Featured Image


# In[34]:


# Visit URL
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[35]:


# Find and click the full image button
full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()


# In[36]:


# Find the more info button and click that
browser.is_element_present_by_text('more info', wait_time=1)
more_info_elem = browser.links.find_by_partial_text('more info')
more_info_elem.click()


# In[37]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[38]:


# find the relative image url
img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel


# In[39]:


# Use the base url to create an absolute url
img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
img_url


# In[40]:


## Mars Facts


# In[51]:


# Visit URL
url = 'http://space-facts.com/mars'
browser.visit(url)


# In[43]:


df = pd.read_html('http://space-facts.com/mars/')[0]
df.head()


# In[44]:


df.columns=['Description', 'Mars']
df.set_index('Description', inplace=True)
df


# In[45]:


df.to_html()


# In[46]:


## Hemispheres


# In[47]:


url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[48]:


hemisphere_image_urls = []

# First, get a list of all of the hemispheres
links = browser.find_by_css("a.product-item h3")

# Next, loop through those links, click the link, find the sample anchor, return the href
for i in range(len(links)):
   hemisphere = {}
   
   # We have to find the elements on each loop to avoid a stale element exception
   browser.find_by_css("a.product-item h3")[i].click()
   
   # Next, we find the Sample image anchor tag and extract the href
   sample_elem = browser.links.find_by_text('Sample').first
   hemisphere['img_url'] = sample_elem['href']
   
   # Get Hemisphere title
   hemisphere['title'] = browser.find_by_css("h2.title").text
   
   # Append hemisphere object to list
   hemisphere_image_urls.append(hemisphere)
   
   # Finally, we navigate backwards
   browser.back()


# In[23]:


hemisphere_image_urls 


# In[ ]:





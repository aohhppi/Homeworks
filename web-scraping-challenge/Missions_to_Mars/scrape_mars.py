

# Import Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd



def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)



def scrape():
    browser = init_browser()

    # Create a dictionary for all of the scraped data
    mars_data = {}

#URL to scrape

    url = 'https://redplanetscience.com'
    browser.visit(url)

#create HTMl Object

    html = browser.html

#parse HTML with beautiful soup

    soup = BeautifulSoup(html, 'html.parser')


# ### NASA Mars News



    nasa_mars_article = soup.find('div', class_='list_text')
    # print(nasa_mars_article)
    # In[10]:
    # Extract title text
    nasa_mars_news_title = soup.find('div',class_='content_title').text
    # nasa_mars_news_title
    # In[11]:
    # Extract Paragraph text
    nasa_mars_news_paragraph = soup.find('div',class_='article_teaser_body').text
    # nasa_mars_news_paragraph

    mars_data["news_article"] = nasa_mars_article
    mars_data["news_title"] = nasa_mars_news_title
    mars_data["summary"] = nasa_mars_news_paragraph

    # ### JPL Mars Space Images—Featured Image

    # In[14]:


    jpl_url = "https://spaceimages-mars.com/"
    browser.visit(jpl_url)
    # In[15]:
    html_image = browser.html
    soup = BeautifulSoup(html_image, 'html.parser')
    # In[16]:
    image_url  = soup.find('img', class_="headerimage fade-in")["src"]
    # image_url
    # In[17]:
    featured_image_url = jpl_url + image_url
    # featured_image_url

    mars_data["featured_image_url"] = featured_image_url
    # ### Mars Facts

    # In[18]:
    # Visit the Mars Facts webpage
    mars_facts='https://galaxyfacts-mars.com'
    browser.visit(mars_facts)
    mars_facts_table = pd.read_html(mars_facts)
    # mars_facts_table


    # In[19]:

    # #Create Dataframe to store table data
    mars_facts_df = mars_facts_table[0]
    mars_facts_df.columns = ['Comparision', 'Mars', 'Earth']
    # mars_facts_df
    mars_data["mars_facts_df"] = mars_facts_df

    # ### Mars Hemispheres

    # In[20]:


    url_hemis = 'https://marshemispheres.com'
    browser.visit(url_hemis)
    # In[21]:
    # Scrap 4 images
    urls = [
        'https://marshemispheres.com/cerberus.html',
        'https://marshemispheres.com/schiaparelli.html',
        'https://marshemispheres.com/syrtis.html',
        'https://marshemispheres.com/valles.html'
    ]
    # create empty dictionary to collect images
    image_data = []
    # In[22]:
    for url in urls:
        print(url)
        # create empty dictionary
        album = {}
            # click link
        browser.visit(url)
            # Scrape the image from the img element
        m_html = browser.html
        m_scraper = BeautifulSoup(m_html, 'html.parser')
            # scrape the title and image url
        m_title = m_scraper.find('h2', {'class': 'title'}).get_text()
            # add title to album
        album['title'] = m_title
        # add image to album
        image_data.append(album)
            # go back a page in the browser
        browser.back()

    mars_data['image_data'] = image_data


    return mars_data






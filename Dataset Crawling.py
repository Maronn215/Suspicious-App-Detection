import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib
import json
import re 


URL = 'https://apps.apple.com/in/genre/ios-games/id6014?letter=Z&page=10#page'
data = urlopen(URL)
soup = BeautifulSoup(data, 'lxml')
url_final = []


for link in soup.find_all(attrs={'class':'column'}):
    for url_info in link.find_all('a'):
        if url_info.get('href').startswith('https://apps.apple.com/in/app/'):
            print ('url=','\t',url_info.get('href'))

      
            url = url_info.get('href')
            res = requests.get(url)
            res.raise_for_status()
            content = res.content
            final_soup = BeautifulSoup(content,'lxml')
            description = str()
            review_ti = str()
            review_co = str()
            title = str()
            age = str()
            relate = str()
            img = str()
            version = str()
            rate = str()
            rating_num = str()
            star = str()
            age_reason = str()
            
            for text in final_soup.find_all('h1',{'itemprop':'name'}):
                title = title+str(text.getText().encode('ASCII', 'ignore').strip()).replace("b'","'").replace('b"','"')    
            
          
            for text in final_soup.find_all('span',{'itemprop':'softwareVersion'}):
                version = version+str(text.getText().encode('ASCII', 'ignore').strip()).replace("b'","'").replace('b"','"')    
            
            for text in final_soup.find_all('p',{'itemprop':'description'}):
                description = description+str(text.getText().encode('ASCII', 'ignore')
                                              .strip()).replace("b'"," ").replace('b"','"')
            for text in final_soup.find_all('span',{'class':'customerReviewTitle'}):
                review_ti = review_ti+str(text.getText().encode('ASCII', 'ignore').strip()).replace("b'"," ").replace('b"','"')
            for text in final_soup.find_all('p',{'class':'content'}):
                review_co = review_co+str(text.getText().encode('ASCII', 'ignore').strip()).replace("b'"," ").replace('b"','"')
            for text in final_soup.find_all('div',{'class':'app-rating'}):
                age = age+str(text.getText().encode('ASCII', 'ignore')
                              .strip()).replace("b'"," ").replace('b"','"').replace("'","")
            
            for text in final_soup.find_all('ul',{'class':'list app-rating-reasons'}):
                age_reason = age_reason+str(text.getText().encode('ASCII', 'ignore').strip()).replace("b'","'").replace('b"','"') 
            
            
            for text in final_soup.find_all('div',{'class':'extra-list more-by'}):
                relate = relate+str(text.getText().encode('ASCII', 'ignore')
                                    .strip()).replace("b'"," ").replace('b"','"').replace('View in Mac App Store','')

       
            for text in final_soup.find_all('meta',{'itemprop':'image'}):
                img = text
                
            for text in final_soup.find_all('span',{'class':'rating-count'}):
                rating_num = rating_num+str(text.getText().encode('ASCII', 'ignore').strip()).replace("b'","'").replace('b"','"')
            
            for text in final_soup.find_all('span',{'itemprop':'ratingValue'}):
                star = star+str(text.getText().encode('ASCII', 'ignore').strip()).replace("b'","'").replace('b"','"') 
            
            

            #print(title)

            with open ('crawler_games.txt','a',encoding='utf-8') as csvfile:
                 csvfile.write(str(title)+'\t'+str(description)+'\t'+str(version)+'\t'+str(review_ti)+'\t'
                               +str(review_co)+'\t'+str(age)+'\t'+str(age_reason)+'\t'+str(relate)+'\t'
                               +str(img)+'\t'+str(rating_num)+'\t'+str(star)+'\n')
            with open ('url_final.txt','a',encoding='utf-8') as csvfile:
                 csvfile.write(str(url)+'\n')

        else:
            continue

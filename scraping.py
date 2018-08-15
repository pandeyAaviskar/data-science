from bs4 import BeautifulSoup
import requests
'''this technique only works if the site u want to scrap is in same directory'''
'''with open('html.html') as hf:
    soup= BeautifulSoup(hf,'lxml')

#match=soup.title.text
match=soup.find('div',class_='h1').text

print(match)'''

'''for online site we use this technique'''
source=requests.get('https://www.facebook.com/').text
soup= BeautifulSoup(source,'lxml')
ab=soup.find('div',class_='_7d _6_ _76').h2.text

print(ab)

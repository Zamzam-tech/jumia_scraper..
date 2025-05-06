from bs4 import BeautifulSoup
import requests

my_url="https://www.geeksforgeeks.org/html-editors/"
response=requests.get(my_url)

print(response)

soup=BeautifulSoup(response.content,'html.parser')

content=soup.find('div', class_="wrapper single-page")
paragraphs=content.find('p')

paragraph_text=paragraphs.text
print(paragraph_text)


#print(paragraphs)



#print(paragraph_text)

#print(paragraphs)

#print(soup.prettify())




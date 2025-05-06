from bs4 import BeautifulSoup
import requests

url='https://www.jumia.co.ke/catalog/?q=smartphones'
response=requests.get(url)
print(response)

Actual_names_list=[]
Actual_prices_list=[]

try:
    if response.status_code==200:
        print("Successfully fetched!")
        soup=BeautifulSoup(response.content,'html.parser')
        content=soup.find('section', class_='card -fh')

        if content:
           product_cards=content.find_all('article', class_='prd _fb col c-prd')
        
           for card in product_cards:
              prices=card.find('div', class_='prc')
         #print(prices)
              if prices:
                 Actual_price=prices.text.strip()
                 Actual_prices_list.append(Actual_price)
    
              else:
                 print("Prices couldn't be fetched.")
                 Actual_prices_list.append(None)

            #Extract the PRODUCT NAMES

                 product_names=card.find('h3',class_='name')

                 if product_names:
                  Actual_names=product_names.text.strip()
                  Actual_names_list.append(Actual_names)
    
                 else:
                  print("PRODUCT NAMES couldn't be fetched")
                  Actual_names_list.append(None)

           print("THE ACTUAL PRODUCT PRICES ARE:",Actual_prices_list)
           print("THE ACTUAL PRODUCT NAMES ARE:",Actual_names_list)     

             
    else:
      print("Sorry COULDN'T fetch content.")
except ImportError:
    print("Content can't be fetched")






    
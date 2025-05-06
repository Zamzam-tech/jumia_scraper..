import pandas as pd
from bs4 import BeautifulSoup
import requests

url = 'https://www.jumia.co.ke/catalog/?q=smartphones'
response = requests.get(url)
print(response)

Actual_names_list = []
Actual_prices_list = []

try:
    if response.status_code == 200:
        print("Successfully fetched!")
        soup = BeautifulSoup(response.content, 'html.parser')
        content = soup.find('section', class_='card -fh')

        if content:
            product_cards = content.find_all('article', class_='prd _fb col c-prd')

            for card in product_cards:
                # Extract price
                prices = card.find('div', class_='prc')
                if prices:
                    Actual_price = prices.text.strip()
                    Actual_prices_list.append(Actual_price)
                else:
                    print("Prices couldn't be fetched.")
                    Actual_prices_list.append(None)

                # Extract the PRODUCT NAMES (moved inside the loop)
                product_names = card.find('h3', class_='name')
                if product_names:
                    Actual_names = product_names.text.strip()
                    Actual_names_list.append(Actual_names)
                else:
                    print("PRODUCT NAMES couldn't be fetched")
                    Actual_names_list.append(None)

            #print("THE ACTUAL PRODUCT PRICES ARE:", Actual_prices_list)
            #print("THE ACTUAL PRODUCT NAMES ARE:", Actual_names_list)

        else:
            print("Could not find the main content section.")
    else:
        print("Sorry COULDN'T fetch content.")
except ImportError:
    print("Content can't be fetched")
except requests.exceptions.RequestException as e:
    print(f"Error fetching URL: {e}")
except AttributeError:
    print("Error: Could not parse the HTML structure as expected.")

if Actual_names_list and Actual_prices_list and len(Actual_prices_list)==len(Actual_names_list):
    #CREATE A DICTIONARY
    data={'Product name':Actual_names_list, 'Product price':Actual_prices_list}

    #Create a data frame
    df=pd.DataFrame(data)
    #print(df)    

    #EXPORTING the data frame into an EXCEL FILE
    excel_filename='jumia_smartphone_data.xlsx'
    df.to_excel(excel_filename,index=False)
    print(f"Data successfully exported to {excel_filename}")

elif not Actual_names_list or not Actual_prices_list:
    print("No data was extracted to create the Data frame")

else:
    print("\nError: The number of product names and prices do not match. Cannot create DataFrame.")

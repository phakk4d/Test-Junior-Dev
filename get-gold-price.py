import requests
from bs4 import BeautifulSoup

url = 'https://chinhuaheng.com/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
#price = soup.find('div', class_ = 'gold-1-ounce').find('span', class_ = 'price').text
price_element = soup.find('div', class_ = 'gold-1-ounce')
if price_element is not None :
    price = price_element.find('span', class_ = 'price').text
    print ('Gold Price : ', price)
else :
    print ('Could not find gold price.')
#print('Gold Price:', price)
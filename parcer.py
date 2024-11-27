'''import requests #--get
response = requests.get("https://httpbin.org/get")
print(response.content)
print(f"Datatype - {type(response.content)}")
print(response.text)
print(f"Datatype - {type(response.text)}")'''

'''import requests *--post
response = requests.post("https://httpbin.org/post", data="Test data",
headers={"h1": "Test title"})
print(response.text)'''

'''import requests #--all datas
response = requests.get("https://coinmarketcap.com/")
print(response.text)'''

'''import requests #--datas inside <span>
response = requests.get("https://coinmarketcap.com/")
response_text = response.text
response_parse = response_text.split("<span>")
for parse_elem_1 in response_parse:
    if parse_elem_1.startswith("$"):
        for parse_elem_2 in parse_elem_1.split("</span>"):
            if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
                print(parse_elem_2)'''

'''import requests #--first elem inside <span>
res_parse_list = []
response = requests.get("https://coinmarketcap.com/")
response_text = response.text
response_parse = response_text.split("<span>")
for parse_elem_1 in response_parse:
    if parse_elem_1.startswith("$"):
        for parse_elem_2 in parse_elem_1.split("</span>"):
            if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
                res_parse_list.append(parse_elem_2)

bitcoin_exchange_rate = res_parse_list[0]
print(bitcoin_exchange_rate)'''

from bs4 import BeautifulSoup #--курс біткоїна з головної сторінки
import requests
response = requests.get("https://coinmarketcap.com/")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("td",{"style":"text-align:end"})
    '''for elem in soup_list:
        print(elem)'''
    res = soup_list[0].find("span")
    print(res.text)

'''from bs4 import BeautifulSoup #--курс біткоїна зі сторінки біткоїна
import requests
response = requests.get("https://coinmarketcap.com/currencies/bitcoin/")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("span",{"data-test":"text-cdp-price-display"})
    for elem in soup_list:
        print(elem.text)'''

'''#--Витягніть всі цитати зі сторінки http://quotes.toscrape.com
from bs4 import BeautifulSoup
import requests
url = 'http://quotes.toscrape.com'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
quotes = soup.find_all('span', {'class': "text"})
for quote in quotes:
    print(quote.text)'''

#--Витягніть всіх авторів цитат зі сайту http://quotes.toscrape.com
from bs4 import BeautifulSoup
import requests
url = 'http://quotes.toscrape.com'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
quotes = soup.find_all('small', {'class': "author"})
for quote in quotes:
    print(quote.text)
#import semua yang kita butuhkan
from datetime import date
from operator import index
from unicodedata import category
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen, Request
from mysql_database import MySqlDB
import pandas as pd

#siapkan semua parameter
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"
headers = {
    'User-Agent': user_agent
}

alamat = "https://indeks.kompas.com/?site=all&date=2021-12-01&page="+str(index)
    
index = 1

while index < 6:
    index+1
    
#request- response
data_request = Request(alamat, headers=headers)
response = urlopen(data_request)

#masukkan dalam objek beautifulsoup
soup = bs(response, "html.parser")

#div, berita
berita = soup.find("div", {"class":"latest--indeks mt2 clearfix"})

titles = berita.find_all("h3", {"class":"article__title article__title--medium"})

list_title = [title.get_text().rstrip() for title in titles]

for i in list_title:
    print(i)
# df = pd.DataFrame(list_title, columns=['Judul Berita'])

# print(df)
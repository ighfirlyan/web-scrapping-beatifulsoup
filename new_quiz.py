#import semua yang kita butuhkan
from datetime import date
from unicodedata import category
from unittest import result
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen, Request
from mysql_database import MySqlDB
import pandas as pd

#siapkan semua parameter
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"
headers = {
    'User-Agent': user_agent
}

# alamat = ["https://indeks.kompas.com/?site=all&date=2021-12-01", 
# 'https://indeks.kompas.com/?site=all&date=2021-12-01&page=2',
# 'https://indeks.kompas.com/?site=all&date=2021-12-01&page=3',
# 'https://indeks.kompas.com/?site=all&date=2021-12-01&page=4',
# 'https://indeks.kompas.com/?site=all&date=2021-12-01&page=5'
# ]


for i in range(1,6):
    alamat = "https://indeks.kompas.com/?site=all&date=2021-12-01&page="+str(i)
    data_request = Request(alamat, headers=headers)
    response = urlopen(data_request)
    #masukkan dalam objek beautifulsoup
    soup = bs(response, "html.parser")
    #div, berita
    berita = soup.find("div", {"class":"latest--indeks mt2 clearfix"})

    titles = berita.find_all("h3", {"class":"article__title article__title--medium"})

    # list_title = [title.get_text().rstrip() for title in titles]

    hasil = []
    for title in titles:
        list_title = title.get_text().rstrip()
        # for i in list_title:
        hasil.append(list_title)

    for i in hasil:
        result=[]
        result.append(i)
        print(result)

df = pd.DataFrame(hasil, columns=['Judul Berita'])
print(df)

    # result=[]
    # for i in hasil:
    #     result.append(i)
    #     print(result)
    
    # df = pd.DataFrame(result, columns=['Judul Berita'])
    # print(df)

    # for index in list_title:
    #     print(index)

    # hasil = []
    # for row in list_title:
    #     for cell in titles:
    #         hasil.append(cell.get_text())

    # print(hasil)

    # df = pd.DataFrame(hasil, columns=['Judul Berita'])
    # print(df)
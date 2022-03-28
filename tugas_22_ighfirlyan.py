#import semua yang kita butuhkan
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen, Request
from mysql_database import MySqlDB
import pandas as pd

#siapkan semua parameter
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"
headers = {
    'User-Agent': user_agent
}

alamat = "https://www.kompas.com/"

#request- response
data_request = Request(alamat, headers=headers)
response = urlopen(data_request)

#masukkan dalam objek beautifulsoup
soup = bs(response, "html.parser")

#div, sidebar-terpopuler 
artikel_populer = soup.find("div", {"class":"most__wrap clearfix"})

titles = artikel_populer.find_all("h4", {"class":"most__title"})

list_title = [title.get_text().rstrip() for title in titles]

df = pd.DataFrame(list_title, columns=['Judul Berita Populer'])

print(df)
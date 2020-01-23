#!/c/Users/jjail/AppData/Local/Microsoft/WindowsApps/python3
import pip._vendor.requests as requests
from bs4 import BeautifulSoup

req = requests.get('https://beomi.github.io/beomi.github.io_old/')
html = req.text

soup = BeautifulSoup(html, 'html.parser')

my_titles = soup.select(
  'h3 > a'
)

for title in my_titles:
    ## Tag안의 텍스트
    print(title.text)
    ## Tag의 속성을 가져오기(ex: href속성)
    print(title.get('href'))


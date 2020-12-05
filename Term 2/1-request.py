import requests

from bs4 import BeautifulSoup
url = "https://bama.ir/car/car/peykan/all-trims?page=1"
data = requests.get(url)
soup=BeautifulSoup(data.txt, "html.parser")
p_tags = soup.find_all('p', class_="shortdesc removeEmoji")
for p_tag in p_tags:
    print(p_tag.text)

import requests
from bs4 import BeautifulSoup 
r = requests.get('https://www.google.org')
soup = BeautifulSoup(r.text,"html.parser")
for heading in soup.find_all("h3"):
    print(heading.text)
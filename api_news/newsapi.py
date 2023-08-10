import requests
import json


URL = f"https://newsapi.org/v2/top-headlines/sources?q=country=us&sortBy=published&apiKey=2dd8fe02c50d42dbafe25fcf0ada1538"

x = requests.get(URL)
news = json.loads(x.text)
y = news["sources"]
print(len(y)) #128

list_news = []
for x in range(0,len(y)):
    list_news.append(y[x]['category'])

list_news = list(set(list_news))

print(f"Present categories are")
dict_news = {}
for x in range(1,len(list_news)+1):
    dict_news[x]=list_news[x-1]
    print(f"{x} : {list_news[x-1]}")

query = int(input("What type of news you want to read = "))
print("\n")


while True:
    for x in range(0,len(y)):
       if dict_news[query] in y[x]['category']:
           print(f"News station : {y[x]['name']}")
           print(f"Heading : {y[x]['description']}")
           print(f"URL : {y[x]['url']}")
           print(f"Country : {y[x]['country']}")
           print("....................")
           print("\n")
    else :
        break
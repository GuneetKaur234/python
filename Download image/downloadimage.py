import requests

url = "https://picsum.photos/200/300"
image = requests.get(url)
open("hello1.jpeg","wb").write(image.content)
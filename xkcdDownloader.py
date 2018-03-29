import bs4
import requests
import os

print("A webcomic of romance, sarcasm, math, and language.")

os.makedirs('xkcd', exist_ok=True)

start = int(input("Enter the starting limit: "))
end = int(input("Enter the end limit: "))

for i in range(start, end + 1):
    res = requests.get("http://xkcd.com/%s" % str(i))
    soup = bs4.BeautifulSoup(res.content, 'html.parser')

    div = soup.find_all('div', {'id': 'comic'})

    image = div[0].find('img')
    src = image.__getitem__("src")[2:]
    comicUrl = os.path.join('http://', src)
    response = requests.get(comicUrl)

    if response.status_code != 404:
        imagefile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        imagefile.write(response.content)
        print("\n", comicUrl)
        print(os.path.basename(comicUrl), "DOWNLOADED")
        i = i + 1
    else:
        print("Image not found...")
        break

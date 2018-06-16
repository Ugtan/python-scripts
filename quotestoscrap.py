""" A small python script to scrap all the quotes from https://quotestoscrap.com and print them all"""

import requests
from bs4 import BeautifulSoup


def QuotesToScrap(pages):
    """ Function to print quotes of every single page"""

    for item in pages:
        response = requests.get(item)
        soup = BeautifulSoup(response.content, "lxml")
        quotes = soup.find_all('div', {'class': 'quote'})
        for q in quotes:
            quote = q.find('span', {'class': 'text'}).text
            author = q.find('small', {'class': 'author'}).text
            print(quote + '\t' + 'by  ' + author)


def main():

    pages = []
    for i in range(1, 11):
        url = "http://quotes.toscrape.com/"
        url = url + "page/{}/".format(i)
        pages.append(url)
    QuotesToScrap(pages)


if __name__ == '__main__':
    main()

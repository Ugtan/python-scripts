"""A small Python script to scrape Top stories of different categories from https://www.indiatoday.in/"""
"""
    Dependencies:
                1. requests
                2. beautifulsoup4
"""

import requests
from bs4 import BeautifulSoup

Choice ={
         "1":"General",
         "2":"Tech",
         "3":"Automobiles",
         "4":"Lifestyle",
         "5":"Sports",
         "6":"Education"
        }

def scrape(url):
    """ To Fetch data from url """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup

def top_stories(soup):
    """ To find the Top Stories using soup object """
    ltags = soup.find("ul", {"class":"itg-listing"}).find_all("li")
    for ltag in ltags:
        atags = ltag.find("a")
        if atags.get("title") != "Contest":
            title = atags.get("title")
            print('* ' + str(title) + '\n')

def tstories(soup):
    """ To find the Top Stories using soup object """
    ltags = soup.find('ul', {"class":"itg-listing"}).find_all("li")
    for ltag in ltags:
            title = ltag.get("title")
            print('* ' + str(title) + '\n')


def main():

    refresh ='y'
    url = 'https://www.indiatoday.in/'
    while refresh == 'y':
        print()
        print(Choice)
        choice = input("\nEnter your choice : ")
        while choice not in ["1","2","3","4","5","6"]:
            print("\nWrong choice! Please enter a valid choice!")
            choice = input("\nEnter your choice : ")

        if choice == "1":
            print("\n\t**General Top Stories**\n")
            soup = scrape(url)
            top_stories(soup)

        if choice == "2":
            print("\n\t**Tech Top Stories**\n")
            soup = scrape(url+'technology')

        if choice == "3":
            print("\n\t**Automobiles Stories**\n")
            soup = scrape(url+'auto')

        if choice == "4":
            print("\n\t**Lifestyle stories**\n")
            soup = scrape(url+'lifestyle')

        if choice == "5":
            print("\n\t**Sports Top Stories**\n")
            soup = scrape(url+'sports')

        if choice == "6":
            print("\n\t**Education Stories**\n")
            soup = scrape(url+'education-today')

        if choice != "1":
            tstories(soup)

        refresh = input('\nDo you want to checkout any other stories?(y/n) ')


if __name__ == '__main__':
    main()

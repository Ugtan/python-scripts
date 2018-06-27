""" A Python Script to display all the Upcoming Cubing Competitions, Competitions around you and Competitions based on the city entered """
"""
DEPENDENCIES: 1. requests
              2. beautifulsoup4
              3. tabulate
              4. termcolor
"""


import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from termcolor import colored


def res(url):
    """ To ping the website using the url for information"""

    response = requests.get(url)
    return response


def location():
    """ To find the location of the current user using his ip address"""

    url = 'https://ipinfo.io/'
    response = res(url)
    data = response.json()
    city = data['city']
    return city


def competitions(soup):
    """ To Find the cubing competitions"""

    data = []
    header = ["DATE", "NAME", "VENUE", "LOCATION"]
    try:

        ul = soup.find("ul", {"class":"list-group"})
        lis = ul.find_all("li")[1:20]
        for li in lis:
            date = li.find("span", {"class":"date"}).text
            name = li.find("div",{"class":"competition-link"}).text
            venue = li.find("div",{"class":"venue-link"}).text
            location = li.find("div",{"class":"location"}).text

            data.append([date, name, venue, location])

        print(colored(tabulate(data, headers = header, tablefmt = 'fancy_grid'), "green"))
    except AttributeError:

        print(colored("\nSorry Bad luck no competitions in your area!", "red", attrs=['blink']))


def main():

    print(colored("\nHey Welcome!", "green", attrs=['blink']))
    print("\n1. Display all the Upcoming Competitions.\
           \n2. Find Competitions around your area. \
           \n3. Find competitions by entering the city.\n")

    choice = input("Enter your choice : ")
    while choice not in map(str,range(1,4)):
        choice = input(colored("\nYou Entered wrong choice! Enter a valid choice.", "red"))

    if choice == "1":
        url = 'https://www.worldcubeassociation.org/competitions'

    elif choice == "2":
        city = location()
        url = 'https://www.worldcubeassociation.org/competitions?utf8=%E2%9C%93&region=all&search={}&state=present&year=all+years&from_date=&to_date=&delegate=&display=list'.format(city)

    else:
        city =input("\nEnter the City! ")
        url = 'https://www.worldcubeassociation.org/competitions?utf8=%E2%9C%93&region=all&search={}&state=present&year=all+years&from_date=&to_date=&delegate=&display=list'.format(city)

    response = res(url)
    soup = BeautifulSoup(response.text , "html.parser")
    competitions(soup)


if __name__ == '__main__':
    main()

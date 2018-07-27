""" A Python Script to display all the Upcoming Cubing Competitions, Competitions around you and Competitions based on the city entered """
"""
DEPENDENCIES: 1. requests
              2. beautifulsoup4
              3. tabulate
              4. termcolor
"""

import getpass
import sys
import requests

from bs4 import BeautifulSoup
from tabulate import tabulate
from termcolor import colored


def res(url):
    """To ping the website using the url for information"""
    response = requests.get(url)
    return response


def location():
    """To find the location of the current user using his ip address"""
    url = 'https://ipinfo.io/'
    response = res(url)
    data = response.json()
    city = data['city']
    return city


def getCompetitions(soup):
    """ To Find the cubing competitions"""
    data = []
    header = ["DATE", "NAME", "VENUE", "LOCATION"]
    try:

        ul = soup.find("ul", {"class": "list-group"})

        print(ul.find("li").text)
        lis = ul.find_all("li")[1:20]
        for li in lis:
            date = li.find("span", {"class": "date"}).text
            name = li.find("div", {"class": "competition-link"}).text
            venue = li.find("div", {"class": "venue-link"}).text
            location = li.find("div", {"class": "location"}).text

            data.append([date, name, venue, location])

        print(colored(tabulate(data, headers=header,
                               tablefmt='fancy_grid'), "green"))
    except AttributeError:

        print(colored("\nSorry Bad luck no competitions in your area!",
                      "red", attrs=['blink']))


def main():
    print(colored("\nHey Welcome!\n", "green", attrs=['blink']))
    args = sys.argv
    args = args[1:]

    if not args:
        print("\nUsage: CubiCom.py COMMAND [ARGS]...\n\n Get Cubing competitions in the command line!\n\nCommands:\n all     Get all the upcoming competitions around the world.\n live    Get all the cubing competions that are in progress.\n nearme    Get all the cubing competions around me.\n [-c] city    Get all the cubing competions that will be held in the city.")
        sys.exit()

    if len(args) < 2:
        if args[0] == "all":
            url = 'https://www.worldcubeassociation.org/competitions'
            response = res(url)
            soup = BeautifulSoup(response.text, "html.parser")
            comps = soup.find("div", {"id": "upcoming-comps"})
            getCompetitions(comps)

        elif args[0] == "live":
            url = 'https://www.worldcubeassociation.org/competitions'
            response = res(url)
            soup = BeautifulSoup(response.text, "html.parser")
            comps = soup.find("div", {"id": "in-progress-comps"})
            getCompetitions(comps)

        elif args[0] == "nearme":
            city = location()
            url = 'https://www.worldcubeassociation.org/competitions?utf8=%E2%9C%93&region=all&search={}&state=present&year=all+years&from_date=&to_date=&delegate=&display=list'.format(
                city)
            response = res(url)
            comps = BeautifulSoup(response.text, "html.parser")
            getCompetitions(comps)

        else:
            print("Sorry, You have entered a wrong command!")

    if len(args) < 3 and args[0] == "-c":
        url = 'https://www.worldcubeassociation.org/competitions?utf8=%E2%9C%93&region=all&search={}&state=present&year=all+years&from_date=&to_date=&delegate=&display=list'.format(
            args[1])
        response = res(url)
        comps = BeautifulSoup(response.text, "html.parser")
        getCompetitions(comps)


if __name__ == '__main__':
    main()

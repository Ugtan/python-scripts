'''
  Dependencies : 1. requests
                 2. beautifulsoup4
                 3. tabulate
                 4. colorclass
'''
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import json
from colorclass import Color


def main():
    username = input(Color("\n{autoblue}Enter your Github Username :{/autoblue} "))
    url = "https://github.com/" + username
    get_contributions(url)
    url = "https://api.github.com/users/{}/repos".format(username)
    get_repos(url)
    url = "https://api.github.com/users/{}/starred".format(username)
    get_starred(url)


def get_contributions(url):
    """To get github contributions """
    my_data = []
    counter = 0
    total = 0
    header = ["S.No", "Date", "Count"]
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    rangles = soup.find_all("rect")
    for rangle in rangles:
        if rangle.get('data-count') != "0":
            date = rangle.get('data-date')
            count = rangle.get('data-count')
            total = total + int(count)
            counter += 1
            my_data.append([counter, date, count])
    print(Color("\n{autogreen}Your Github Contributions: {/autogreen} \n"))
    print(tabulate(my_data, headers=header, tablefmt="fancy_grid"))
    print(Color("\n{autogreen}Total Contributions : %d {/autogreen} \n" % total))


def get_repos(url):
    """ To get the total number of repos user has"""
    response = requests.get(url)
    data = response.text
    data = json.loads(data)
    my_data = []
    header = ["S.No", "Repostitory"]

    for count, repos in enumerate(range(len(data)), 1):
        my_data.append([count, data[repos]['name']])
    print(Color("{autogreen}Your Repositories!{/autogreen}\n"))
    print(tabulate(my_data, headers=header, tablefmt="fancy_grid"))


def get_starred(url):
    """ To get user's starred repos"""
    response = requests.get(url)
    data = response.text
    data = json.loads(data)
    my_data = []
    header = ["S.No", "Starred Repository", "Owner of Repo"]

    for count, starred in enumerate(range(len(data)), 1):
        Srepo, owner = data[starred]['full_name'].split('/')
        my_data.append([count, Srepo, owner])
    print(Color("\n{autogreen}Your Starred Repositories!{/autogreen}\n"))
    print(tabulate(my_data, headers=header, tablefmt="fancy_grid"))


if __name__ == '__main__':
    main()

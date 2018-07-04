""" CricRatings is a python script to find the team and player ratings for both men and women"""
""" Dependencies: 1. requests
                  2. pandas
                  3. beautifulsoup4
                  4. tabulate
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup
from tabulate import tabulate

URL = "https://www.icc-cricket.com/rankings/"


def Soup(url):
    """ To return a soup object"""
    res = requests.get(url)
    return BeautifulSoup(res.content, "lxml")


def category(choice):
    """ To return test or odi or t20i based on what the user has entered"""
    return {
             "1": "test",
             "2": "odi",
             "3": "t20i"
    }[choice]


def forte(choice):
    """ To return the forte of the player selected by the user"""
    return {
             "1": "batting",
             "2": "bowling",
             "3": "all-rounder"
    }[choice]


def gender(choice):
    """ To return the gender selected by the user"""
    return {
             "1": "mens",
             "2": "womens"
    }[choice]


def rankings(soup):
    """ To find the team or player rankings of the respective categories"""
    try:
        table = soup.find("table")
        df = pd.read_html(str(table))
        pretty = tabulate(df[0], headers = 'keys', tablefmt ='fancy_grid', showindex ='never')
        print(pretty)
    except ValueError:
        print("No tables found for the choosen category!")

def main():

    print("\n\t\tHey! Welcome to CricRatings.\n")

    ranking = input("Do you want to check:\
        1. Team Rankings\
        2. Player Rankings\
        \nEnter your choice: ")

    while ranking not in map(str, range(1,3)):
        ranking = input("\nPlease enter a valid choice! ")

    gender_choice = input("\nYou want to checkout rankings of:\
        1. Men\
        2. Women\
        \nEnter your choice: ")

    while gender_choice not in map(str, range(1,3)):
        gender_choice = input("\nPlease enter a valid choice! ")


    choice = input("\nYou want to see rankings for:\
        1. Tests\
        2. ODI\
        3. T20I\
        \nEnter your choice: ")

    while choice not in map(str, range(1,4)):
        choice = input("\nPlease enter a valid choice! ")

    if ranking == "1":
        if gender_choice == "1":
            url = URL + gender(gender_choice)+'/team-rankings/' + category(choice)
        else:
            url = URL + gender(gender_choice)+'/team-rankings/'

    else:
        forte_choice = input("\nChoose one of the following:\
            1. Batting\
            2. Bowling\
            3. All-Rounder\
            \nEnter your choice: ")

        while forte_choice not in map(str, range(1,4)):
            forte_choice = input("\nPlease enter a valid choice! ")
        url = URL + gender(gender_choice) + '/player-rankings/' + category(choice) + '/' + forte(forte_choice)

    soup = Soup(url)
    rankings(soup)


if __name__ == '__main__':
    main()

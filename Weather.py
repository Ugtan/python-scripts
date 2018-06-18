""" It is a small python script to check the weather of your current location(or any other city) using user's ip address and OpenWeatherMap API"""

""" IMPORTANT:
* To run this script you will first have to sign up on https://home.openweathermap.org/users/sign_up
* This is necessary to use their APIs
* Then get the api key and replace it in the below code under appid in the urls below
* Install requests if not already using : pip3 install requests
"""

import requests

CHOICE = {"1":"Find weather by using my location.",
          "2":"Find weather of the city entered"}

def res(url):
    """ To ping the website using the url for information"""

    response = requests.get(url)
    data = response.json()
    return data

def location():
    """ To find the location of the current user using his ip address"""

    url = 'https://ipinfo.io/'
    data = res(url)
    city = data['city']
    location = data['loc'].split(',')
    latitude = location[0]
    longitude = location[1]
    return latitude,longitude


def weather(*args):
    """ To find the weather of that current location"""

    if len(args)==1:
        city = args[0]
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=d5cba1979a99f72e6014b8127038248c&units=metric'.format(city)

    else:
        lat = args[0]
        lon = args[1]
        url = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=d5cba1979a99f72e6014b8127038248c&units=metric'.format(lat, lon)

    data = res(url)
    temp = data['main']['temp']
    humidity= data['main']['humidity']
    pressure = data['main']['pressure']
    wspeed = data['wind']['speed']
    wdegree = data['wind']['deg']
    longitude = data['coord']['lon']
    latitude = data['coord']['lat']
    desc = data['weather'][0]['description']
    city = data['name']

    print("\nCity : {}".format(city))
    print("\nLatitude : {} degrees".format(latitude))
    print("\nLongitude : {} degrees".format(longitude))
    print("\nTemperature : {} degree celcius".format(temp))
    print("\nHumidity : {} g/m^3".format(humidity))
    print("\nPressure : {} mBar".format(pressure))
    print("\nWind Speed : {} mph".format(wspeed))
    print("\nWind degree : {} degrees".format(wdegree))
    print("\nDescription : {}".format(desc))


def main():

    print(CHOICE)
    choice = input("Enter your choice : ")
    while choice not in ["1","2"]:
        print("\nYou Entered wrong choice! Enter a valid choice.")
        choice = input("Enter your choice : ")

    if choice == "1":
        lat, lon = location()
        weather(lat, lon)
    else:
        city = input("Enter the city : ")
        weather(city)


if __name__ == '__main__':
    main()

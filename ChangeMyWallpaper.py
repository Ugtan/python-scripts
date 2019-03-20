'''
A script to download wallpaper from https://wallpaperscraft.com/ and store the image and set the image
as your desktop wallpaper. Jsscript link- https://git.reviewboard.kde.org/r/125648/

I use KDE plasma, it is very likely that it will work only on KDE.

'''

import dbus
import random
import requests
import os
import subprocess

from bs4 import BeautifulSoup

URL = "https://wallpaperscraft.com/catalog/3d/1920x1080/page%s"

jsscript = '''
var allDesktops = desktops();
print (allDesktops);
for (i=0;i<allDesktops.length;i++) {
    d = allDesktops[i];
    d.wallpaperPlugin = "org.kde.image";
    d.currentConfigGroup = Array("Wallpaper", "org.kde.image", "General");
    d.writeConfig("Image", "file://%s")
}
'''


def get_wallpaper():
    """
    Function to download the wallpaper and store it in Pictures directory \
    and returns the path where image is stored
    """
    path = os.path.expanduser('~') + '/Pictures/'
    page = random.randint(1,50)
    url = URL % page
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    imgNum = random.randint(0,14)
    link = soup.find_all("a", {"class": "wallpapers__link"})[imgNum].get('href')
    response = requests.get('https://wallpaperscraft.com' + link)
    soup = BeautifulSoup(response.text, 'html.parser')
    imgSrc = soup.find("img", {"class": "wallpaper__image"}).get('src')
    command = ["wget", "-P", path, imgSrc]
    subprocess.run(command)
    return path + imgSrc.split('/')[-1]

def change_wallpaper(filePath):
    """
    Function takes the file path as argument and changes the Desktop wallpaper
    """
    bus = dbus.SessionBus()
    plasma = dbus.Interface(bus.get_object('org.kde.plasmashell', '/PlasmaShell'), dbus_interface='org.kde.PlasmaShell')
    result = plasma.evaluateScript(jsscript % (filePath))
    print('Done!')

if __name__ == "__main__":
    filePath = get_wallpaper()
    change_wallpaper(filePath)


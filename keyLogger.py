import os
from pynput.keyboard import Key, Listener

if not os.path.exists('/home/umang/python-scripts/test.txt'):
    os.mknod('/home/umang/python-scripts/test.txt')

file = open("test.txt", "w")
combination = {Key.alt and Key.tab}


def on_press(key):
    if key in combination:
        print("Writing to file... ")
    file.write(str(key))


def on_release(key):
    if key == Key.esc:
        file.close()
        listener.stop()


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

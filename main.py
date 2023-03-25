import time
from pynput.keyboard import Key, Controller
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

print("Which mode would you like ?\n"
      "Press 1 if you want to \"/fullmute all\"\n"
      "Press 2 if you want to \"/mute all\"")
print("Press key:", end="")
mode = input()
if mode.isdecimal():
    mode = int(mode)

if mode == 1:
    print("mode=1 \"/fullmute all\"")
else:
    print("mode=2 \"/mute all\"")


mute = False

in_game = True

def send_message(message):
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.02)
    keyboard.type(message)
    time.sleep(0.02)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.02)


while 1:
    keyboard = Controller()
    try:
        request_pseudo = requests.get(
            'https://127.0.0.1:2999/liveclientdata/activeplayername', verify=False)
        your_pseudo = request_pseudo.json()
        response_API = requests.get(f'https://127.0.0.1:2999/liveclientdata/playerscores?summonerName={your_pseudo}',
                                    verify=False)
        statistics = response_API.json()
        if request_pseudo and response_API and not in_game:
            print("Game found!")
            in_game = True

        deaths = statistics['deaths']

        if deaths > 0 and not mute:
            if mode == 1:
                send_message("/fullmute all")
            else:
                send_message("/mute all")
            mute = True

        time.sleep(1)
    except:
        if in_game:
            print("Searching for game...")
        in_game = False
        mute = False

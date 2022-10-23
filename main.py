import requests
import json
import time


def check_twitch():
    with open('usernames.txt') as file:
        for line in file:
            twitch_available(line.rstrip())
    print("\nAll available usernames can be found in available_twitch.txt")
    time.sleep(3)


def twitch_available(user):
    response = requests.get("https://passport.twitch.tv/usernames/"+user)
    if response.status_code == 204:
        with open('available_twitch.txt', 'a+') as f:
            f.write('\n'+user)


def check_steam():
    with open('config.json', 'r') as f:
        config = json.load(f)
    if config["steam_apikey"] == "Enter apikey here":
        print("\nPlease enter your steam apikey in config.json")
        time.sleep(3)
        return
    apikey = config["steam_apikey"]
    with open('usernames.txt') as file:
        for line in file:
            steam_available(line.rstrip(), apikey)
    print("\nAll available usernames can be found in available_steam.txt")
    time.sleep(3)


def steam_available(user, apikey):
    response = requests.get(f"http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={apikey}&vanityurl="+user)
    data = response.json()
    if data["response"]["success"] == 42:
        with open('available_steam.txt', 'a+') as f:
            f.write('\n'+user)


def clear():
    with open('available_twitch.txt', "w") as f:
        f.write("Available twitch usernames:")
        f.close()
    with open('available_steam.txt', "w") as f:
        f.write("Available steam vanity urls:")
        f.close()


def selection():
    print("Where do you want to check the usernames?")
    print("Note: You need a valid apikey for steam.")
    val = input("\n[S]= Steam | [T]= Twitch | [A]= All : ")
    if val == "A":
        check_twitch()
        check_steam()
    elif val == "S":
        check_steam()
    elif val == "T":
        check_twitch()


def main():
    clear()
    selection()


main()

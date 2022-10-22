import requests


def check(user):
    response = requests.get("https://passport.twitch.tv/usernames/"+user)
    if response.status_code == 204:
        with open('available.txt', 'a+') as f:
            f.write('\n'+user)


def clear():
    with open('available.txt', "w") as f:
        f.write("Available users:")
        f.close()


def main():
    clear()
    with open('usernames.txt') as file:
        for line in file:
            check(line.rstrip())


main()

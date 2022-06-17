try:
    import requests
    import pyfiglet
    import ctypes
    from pathlib import Path
    import requests
    import random
except ImportError:
    input("Error while importing modules. Please install the modules in requirements.txt")

class bcolors:
    PURPLE = '\033[0;35m'
    WHITE = '\033[0;37m'
    GREEN = '\033[0;32m'
    RED = '\033[0;31m'

class prefixes:
    CONSOLE = bcolors.PURPLE + "[Console] " + bcolors.WHITE
    AVAILABLE = bcolors.GREEN + "[Available] " + bcolors.WHITE 
    UNAVAILABE = bcolors.RED + "[Unavailable] " + bcolors.WHITE
    ERROR = bcolors.RED + "[Error] " + bcolors.WHITE

def __init__(self):
        self.unavailable = 0
        self.available = 0

def main():
        ctypes.windll.kernel32.SetConsoleTitleW("TikTokChecker | @Jxzper on GitHub")
        ascii_banner = pyfiglet.figlet_format("TiktokChecker")
        print(bcolors.PURPLE + ascii_banner)
        print(prefixes.CONSOLE + "1. Check from list")
        print(prefixes.CONSOLE + "2. Check random names from provided info")
        optionInput = input(prefixes.CONSOLE + "Option: ")

        print("")

        if optionInput == "1":
            usernameFilePath = Path("usernames.txt")
            if not usernameFilePath.is_file():
                usernameFile = open(usernameFilePath, "w")
                usernameFile.close()

            print(prefixes.CONSOLE + "Enter your list in usernames.txt")
            input(prefixes.CONSOLE + "Press Enter if you want to continue..")
            print("")

            usernames = []
            try:
                with open('usernames.txt') as f:
                    for line in f:
                        usernames.append(line)
            except :
                input(prefixes.ERROR + "Something went wrong while trying to retrieve list..")

            print(prefixes.CONSOLE + "Generating usernames..")
            start(usernames)

        elif optionInput == "2":
            valid = False
            amount = 0
            length = 0
            while not valid:
                try:
                    amount =  int(input(prefixes.CONSOLE + "How many names do you want to generate?: "))
                    length = int(input(prefixes.CONSOLE + "How long do you want the names to be?: "))
                    valid = True
                except ValueError:
                    print(prefixes.ERROR + 'Please only input digits..')
            
            print("")
            print(prefixes.CONSOLE + "Choose a character string")
            print(prefixes.CONSOLE + "1. \"abcdefghijklmnopqrstuvwxyz1234567890\"")
            print(prefixes.CONSOLE + "2. \"abcdefghijklmnopqrstuvwxyz\"")
            print(prefixes.CONSOLE + "3. Custom")

            choice = 0
            chars = ""
            valid_ = False

            while not valid_:
                try:
                    choice = int(input(prefixes.CONSOLE + "Option: "))
                    if int is 1 or 2 or 3:
                        valid_ = True
                except:
                    print(prefixes.ERROR + 'Choose a valid option..')
            if choice == 1:
                chars = "abcdefghijklmnopqrstuvwxyz1234567890"
            elif choice == 2:
                chars = "abcdefghijklmnopqrstuvwxyz" 
            elif choice == 3:
                chars = input(prefixes.CONSOLE + "Enter character string: ")

            print(prefixes.CONSOLE + "Generating usernames..")
            usernames = []
            for i in range(amount):
                name = ''.join(random.choice(chars) for i in range(length))
                usernames.append(name)
            print(prefixes.CONSOLE + "Generated " + str(length) + " names!")

            print(prefixes.CONSOLE + "Checking usernames..")
            start(usernames)

        else:
            print("choose a real option." )

def write_file(arg: str) -> None:
    with open('hits.txt', 'a', encoding='UTF-8') as f:
        f.write(f'{arg}\n')

def _check(session: requests.session, username: str):
        username = username.strip()
        response = session.get(f'https://www.tiktok.com/@{username}', headers={'Accept': 'application/xml; charset=utf-8','User-Agent':'foo'})
        if response.status_code == 200 and len(username) > 2:
            print(prefixes.UNAVAILABE + username)
        else:
            print(prefixes.AVAILABLE + username)
            write_file(username)

def start(usernames):
    print(prefixes.CONSOLE + 'Loading..')
    sess = requests.session()
    for u in usernames:
        _check(sess,u)
    print(prefixes.CONSOLE + 'Done checking list!')

if __name__ == '__main__':
    main()
    input()

import os
import fade
import nmap
from colorama import Fore, Style, init
import re
from ping3 import ping
from colorama import Fore, init  
import random
import getpass 
import string 
import requests

init(autoreset=True)

def display_ascii_logo():
    logo_text = """ 
                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~
    """
    faded_text = fade.fire(logo_text)
    print(faded_text)


init()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_nitro_code():
    """Generate a Discord Nitro Code."""
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
    return f'https://discord.gift/{code}'

def nitro_code_generator():
    """Generate Discord Nitro Codes."""
    try:
        clear_screen()
        print(Fore.LIGHTYELLOW_EX + "+" + "-" * 52 + "+")
        print(Fore.LIGHTYELLOW_EX + "{:<50}".format("Nitro Code Generator"))
        print(Fore.LIGHTYELLOW_EX + "+" + "-" * 52 + "+")
        num_codes = int(input("Enter the number of Nitro codes to generate: "))
        for _ in range(num_codes):
            nitro_code = generate_nitro_code()
            print(Fore.LIGHTYELLOW_EX + nitro_code)
        print(Fore.LIGHTYELLOW_EX + "+" + "-" * 52 + "+")
        input("Press Enter to return to the main menu...")
    except Exception as e:
        print(f"An error occurred: {e}")
        input("Press Enter to return to the main menu...")

def generate_roblox_code():
    """Generate a Roblox code."""
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    return f'https://www.roblox.com/promocodes/redeem/{code}'

def generate_roblox_code():
    """Generate a Roblox code."""
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    return f'https://www.roblox.com/promocodes/redeem/{code}'

def check_roblox_code(code):
    """Check if a Roblox code is valid."""
    url = f"https://www.roblox.com/promocodes/redeem/{code}"
    response = requests.get(url)
    if response.status_code == 200:
        return True
    else:
        return False

def roblox_code_generator_and_checker():
    """Generate and Check Roblox Codes."""
    try:
        clear_screen()
        print(Fore.LIGHTYELLOW_EX + "+" + "-" * 52 + "+")
        print(Fore.LIGHTYELLOW_EX + "{:<50}".format("Roblox Code Generator & Checker"))
        print(Fore.LIGHTYELLOW_EX + "+" + "-" * 52 + "+")
        num_codes = int(input("Enter the number of Roblox codes to generate and check: "))
        for _ in range(num_codes):
            roblox_code = generate_roblox_code()
            valid = check_roblox_code(roblox_code.split("/")[-1])
            if valid:
                print(Fore.LIGHTYELLOW_EX + f"{roblox_code} - Valid")
            else:
                print(Fore.LIGHTYELLOW_EX + f"{roblox_code} - " + Fore.RED + "Invalid")
        print(Fore.LIGHTYELLOW_EX + "+" + "-" * 52 + "+")
        input("Press Enter to return to the main menu...")
    except Exception as e:
        print(f"An error occurred: {e}")
        input("Press Enter to return to the main menu...")

def main():
    while True:
        display_ascii_logo()
        print(f"{fade.fire('         ╔═══                                    ═══╗')}")
        print(f"{fade.fire('                                                     ')}")
        print(f"{fade.fire('                [1] Nitro gen           [2] Roblox gen                     ')}")
        print(f"{fade.fire('                [3]                     [4]                         ')}")
        print(f"{fade.fire('                [5]                     [6]      ')}")
        print(f"{fade.fire('         ╚═══                                    ═══╝')}")
        choice = input("[<>] ")

        if choice == "1":
            nitro_code_generator()
        elif choice == "2":
            roblox_code_generator_and_checker()
        elif choice == "0":
            print("Exit")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

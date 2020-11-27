import requests
import threading
import os
from colorama import Fore
from itertools import cycle
os.system('color')



print(f"""
{Fore.LIGHTCYAN_EX}
██╗░░░██╗░██████╗███████╗██████╗░███╗░░██╗░█████╗░███╗░░░███╗███████╗
██║░░░██║██╔════╝██╔════╝██╔══██╗████╗░██║██╔══██╗████╗░████║██╔════╝
██║░░░██║╚█████╗░█████╗░░██████╔╝██╔██╗██║███████║██╔████╔██║█████╗░░
██║░░░██║░╚═══██╗██╔══╝░░██╔══██╗██║╚████║██╔══██║██║╚██╔╝██║██╔══╝░░
╚██████╔╝██████╔╝███████╗██║░░██║██║░╚███║██║░░██║██║░╚═╝░██║███████╗
░╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝

░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝ --- by WRLD#1266""")
print(f'[1] Username:Cookie Format\n[2] Cookie:Username Format')
print('\n')
choice = input(f'>>>> {Fore.RESET}')
amount = 0

with open('cookies.txt','r+', encoding='utf-8') as f:
    cookie = cycle(f.read().splitlines())
with open('proxies.txt', 'r+', encoding='utf-8') as f:
    proxy = cycle(f.read().splitlines())

def usernamechecker():
    while True:
        try:
            cookieCHECK = next(cookie)
            cookies = {'.ROBLOSECURITY': cookieCHECK}

            proxies = {
                'https': 'https://' + next(proxy)
            }
            checkuser = requests.get('https://www.roblox.com/mobileapi/userinfo', cookies=cookies, proxies=proxies)
            usernam = checkuser.json()['UserName']

            if checkuser.status_code == 200:
                readcookies = open('usernames.txt', 'r').read().split('\n')
                with open('usernames.txt', 'a+') as f:
                    if f'{usernam}:{cookieCHECK}' in readcookies:
                        print(f'{Fore.RED}[ - ] Error: Cookie already in file{Fore.RESET}')
                    else:
                        print(f'{Fore.LIGHTCYAN_EX}[ + ] Username: {usernam} Cookie: {cookieCHECK}')
                        f.write(f'{usernam}:{cookieCHECK} \n')
            else:
                print(f'{Fore.RED}[ - ] Dead Proxy, Retrying. . .{Fore.RESET}')

        except Exception as err:
            print(f'{Fore.RED}[ - ] Error: {err}{Fore.RESET}')
def usernamechecker1form():
    while True:
        try:
            cookieCHECK = next(cookie)
            cookies = {'.ROBLOSECURITY': cookieCHECK}

            proxies = {
                'https': 'https://' + next(proxy)
            }
            checkuser = requests.get('https://www.roblox.com/mobileapi/userinfo', cookies=cookies, proxies=proxies)
            usernam = checkuser.json()['UserName']

            if checkuser.status_code == 200:
                readcookies = open('usernames.txt', 'r').read().split('\n')
                with open('usernames.txt', 'a+') as f:
                    if f'{cookieCHECK}:{usernam}' in readcookies:
                        print(f'{Fore.RED}[ - ] Error: Cookie already in file{Fore.RESET}')
                    else:
                        print(f'{Fore.LIGHTCYAN_EX}[ + ] Username: {usernam} Cookie: {cookieCHECK}')
                        f.write(f'{cookieCHECK}:{usernam} \n')
            else:
                print(f'{Fore.RED}[ - ] Dead Proxy, Retrying. . .{Fore.RESET}')

        except Exception as err:
            print(f'{Fore.RED}[ - ] Error: {err}{Fore.RESET}')
if choice == '1':
    num = int(input(f'{Fore.LIGHTCYAN_EX}Threads: {Fore.RESET}'))
    for i in range(num):
        t1 = threading.Thread(target=usernamechecker).start()
if choice == '2':
    num = int(input(f'{Fore.LIGHTCYAN_EX}Threads: {Fore.RESET}'))
    for i in range(num):
        t1 = threading.Thread(target=usernamechecker1form).start()

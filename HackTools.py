from colorama import Fore, Style
import time
import os

def code1():
    os.system("cls")
    os.system("clear")
    print(Style.RESET_ALL+f"""Перед запуском введите {Fore.GREEN}код аутентификации{Style.RESET_ALL}.
    {Fore.RED}99{Style.RESET_ALL}. Где найти код?""")
    code = input("Введите значение: ")
    if code == "99":
        print(Style.RESET_ALL+f"\nНайти код вы можете в этом телеграм канале - {Fore.RED}https://teleg.run/hacktools666{Style.RESET_ALL}\nПост с кодом будет в закреплённом сообщении")
        code2 = input("Введите код: ")
        if code2 == "f5d73f159d742ea3e8b1d64febd54279": #MD5 HASH
            print("[💚] Запуск...")
            time.sleep(1)
            from core import exe
            pass

        else:
            print("[💤] Введен неверный код.")
            time.sleep(3)
            code1()

    if code == "f5d73f159d742ea3e8b1d64febd54279": #MD5 HASH
        print("[💚] Запуск...")
        time.sleep(1)
        from core import exe
        pass


    else:
        print("[💤] Введен неверный код.")
        time.sleep(3)
        code1()
code1()
# -*- coding: utf-8 -*-
import os
import time
from time import sleep
from colorama import Fore, Back, Style
#Автор - x11repo#
#При копипасте пожалуйста указывайте меня как Автора и не удаляйте эти строки#
#Кстати если знаешь нормальный обфускатор напиши мне - vk.com/x11repo#

def menu():
	os.system("clear")
	print(Fore.GREEN+f"╔╗ ╔╗        ╔╗  ╔════╗        ╔╗")
	print(Fore.GREEN+f"║║ ║║        ║║  ║╔╗╔╗║        ║║")
	print(Fore.GREEN+f"║╚═╝║╔══╗╔══╗║║╔╗╚╝║║╚╝╔══╗╔══╗║║ ╔══╗")
	print(Fore.GREEN+f"║╔═╗║║╔╗║║╔═╝║╚╝╝  ║║  ║╔╗║║╔╗║║║ ║══╣")
	print(Fore.GREEN+f"║║ ║║║╔╗║║╚═╗║╔╗╗  ║║  ║╚╝║║╚╝║║╚╗╠══║")
	print(Fore.GREEN+f"╚╝ ╚╝╚╝╚╝╚══╝╚╝╚╝  ╚╝  ╚══╝╚══╝╚═╝╚══╝{Style.RESET_ALL}")
	print(Fore.GREEN+f"{Fore.BLUE}======================================")
	print(Fore.GREEN+f"{Style.RESET_ALL}Created By x11repo a.k.a Aqua.")
	print(Fore.GREEN+f"{Style.RESET_ALL}Web-site: x11repo.site")
	print(Fore.GREEN+f"{Style.RESET_ALL}Ver: 1.0")
	print(Fore.GREEN+f"{Fore.BLUE}======================================")
	print(Fore.GREEN+f"{Style.RESET_ALL}00. Установить всё.")
	print(Fore.BLUE+f"--------------------------------------"+Style.RESET_ALL)
	time.sleep(0.5)
	print(Fore.GREEN+f"{Style.RESET_ALL}1. Установить {Fore.GREEN}Nmap")
	time.sleep(0.5)
	print(Fore.GREEN+f"{Style.RESET_ALL}2. Установить {Fore.GREEN}Hydra")
	time.sleep(0.5)
	print(Fore.GREEN+f"{Style.RESET_ALL}3. Установить {Fore.GREEN}SQLMap")
	time.sleep(0.5)
	print(Fore.GREEN+f"{Style.RESET_ALL}4. Установить {Fore.GREEN}Metasploit")
	time.sleep(0.5)
	print(Fore.GREEN+f"{Style.RESET_ALL}5. Установить {Fore.GREEN}ngrok")
	time.sleep(0.5)
	print(Fore.GREEN+f"{Style.RESET_ALL}6. Установить {Fore.GREEN}Kali Nethunter")
	time.sleep(0.5)
	print(Fore.GREEN+f"{Style.RESET_ALL}7. Установить {Fore.GREEN}angryFuzzer")
	time.sleep(0.5)
	print(Fore.GREEN+f"{Style.RESET_ALL}8. Установить {Fore.GREEN}Red_Hawk")
	time.sleep(0.5)
	print(Fore.GREEN+f"{Style.RESET_ALL}9. Установить {Fore.GREEN}Weeman")
	time.sleep(0.5)
	print(Fore.GREEN+f"{Style.RESET_ALL}10. Установить {Fore.GREEN}IPGeoLocation")
	time.sleep(0.5)
	print(Fore.GREEN+f"{Style.RESET_ALL}11. Установить {Fore.GREEN}Cupp")
	time.sleep(0.5)
	print(Fore.GREEN+f"{Style.RESET_ALL}12. Instagram {Fore.GREEN}Bruteforcer (instahack)")
	time.sleep(0.5)
	print(Fore.GREEN+f"{Style.RESET_ALL}13. Twitter {Fore.GREEN}Bruteforcer   (TwitterSniper)")
	time.sleep(0.5)
	print(Fore.GREEN+f"{Style.RESET_ALL}14. Установить {Fore.GREEN}Ubuntu")
	time.sleep(0.5)
	print(Fore.GREEN+f"{Style.RESET_ALL}15. Установить {Fore.GREEN}Fedora")
	time.sleep(0.5)
	print(Fore.GREEN+f"{Style.RESET_ALL}16. Установить {Fore.GREEN}viSQL")
	time.sleep(0.5)
	print(Fore.GREEN+f"{Style.RESET_ALL}17. Установить {Fore.GREEN}Hash-Buster")
	time.sleep(0.5)
	print(Fore.GREEN+f"{Style.RESET_ALL}18. Установить {Fore.GREEN}D-TECT")
	time.sleep(0.5)
	print(Fore.GREEN+f"{Style.RESET_ALL}19. Установить {Fore.GREEN}routersploit")
	time.sleep(0.5)
	print(Fore.BLUE+f"------------------------------------------"+Style.RESET_ALL)
	print(Fore.GREEN+f"{Style.RESET_ALL}99. {Fore.RED}Выход.{Fore.BLUE}")
	print(Fore.BLUE+f"=========================================="+Style.RESET_ALL)

loop = True

while loop:
    menu()
    what = input("$ >  ")
    if what == "00":
        print("================================")
        hm = input(Fore.GREEN+f"{Style.RESET_ALL}[?] Вы уверенны что хотите установить всё? ({Fore.GREEN}y{Style.RESET_ALL}/{Fore.RED}n{Style.RESET_ALL}): ")
        print("================================")
        if hm == "y":
            print(Fore.BLUE+f"\n========================================================"+Style.RESET_ALL)
            print("[+] Можешь свернуть терминал и идти смотреть мультики...")
            print("Потому-что это займёт много времени.")
            print(Fore.BLUE+f"========================================================"+Style.RESET_ALL)
            print(Fore.WHITE+f"{Back.RED}\nНо лучше следить за установкой, так-как при клонировании будет спрашивать логин и пароль от гитхаба"+Style.RESET_ALL)
            time.sleep(5)
            os.system("apt-get update")
            os.system("apt-get install -y git")
            os.system("apt-get install -y python")
            os.system("apt-get install -y python2")
            os.system("apt-get install -y wget")
            os.system("apt-get install -y nmap")
            os.system("plg install -y hydra ")
            os.system("apt-get update -y")
            os.system("apt-get install -y git")
            os.system("apt-get install python2")
            os.system("cd && git clone https://github.com/sqlmapproject/sqlmap.git")
            os.system("cd")
            os.system("apt-get install wget")
            os.system("cd && wget https://Auxilus.github.io/metasploit.sh")
            os.system("cd && bash metasploit.sh")
            os.system("cd && cd metasploit-framework")
            os.system("cd && gem install bundle --pre")
            os.system("cd && bundle config build.nokogiri --use-system-libraries")
            os.system("cd && bundle install")
            os.system("cd")
            os.system("apt-get update -y")
            os.system("apt-get install -y git")
            os.system("cd && git clone https://github.com/themastersunil/ngrok.git")
            os.system("cd")
            os.system("apt-get update -y")
            os.system("apt-get install -y git")
            os.system("apt-get install -y python2")
            os.system("cd && git clone https://github.com/ihebski/angryFuzzer.git")
            os.system("cd && cd angryFuzzer")
            os.system("cd && pip2 install -r requirements.txt")
            os.system("cd && pip2 install requests")
            os.system("cd")
            os.system("apt-get update -y")
            os.system("apt-get install -y git")
            os.system("apt-get install -y php")
            os.system("cd && git clone https://github.com/Tuhinshubhra/RED_HAWK")
            os.system("cd")
            os.system("apt-get update -y")
            os.system("apt-get install -y python2")
            os.system("apt-get install -y git")
            os.system("cd && git clone https://github.com/evait-security/weeman.git")
            os.system("cd && cd weeman")
            os.system("cd && chmod +x weeman.py")
            os.system("cd")
            os.system("apt-get update -y")
            os.system("apt-get install -y git")
            os.system("apt-get install -y python")
            os.system("cd && git clone https://github.com/maldevel/IPGeoLocation.git")
            os.system("cd && cd IPGeoLocation")
            os.system("cd && pip install -r requirements.txt")
            os.system("cd")
            os.system("apt-get update -y")
            os.system("apt-get install -y git")
            os.system("apt-get install -y python")
            os.system("cd && git clone https://github.com/Mebus/cupp.git")
            os.system("apt-get update -y")
            os.system("apt-get install -y git")
            os.system("apt-get install -y python")
            os.system("apt-get install -y nano")
            os.system("pip install requests")
            os.system("pip install beautifulsoup4")
            os.system("cd && git clone https://github.com/avramit/instahack.git")
            os.system("apt-get update -y")
            os.system("apt-get install -y git")
            os.system("apt-get install -y python")
            os.system("pip install mechanicalsoup")
            os.system("apt-get install -y nano")
            os.system("cd && git clone https://github.com/abdallahelsokary/TwitterSniper.git")
            os.system("apt-get update -y")
            os.system("apt-get install -y git")
            os.system("apt-get install -y python2")
            os.system("cd && git clone https://github.com/blackvkng/viSQL.git")
            os.system("apt-get update -y")
            os.system("apt-get install -y git")
            os.system("apt-get install -y python2")
            os.system("cd && git clone https://github.com/UltimateHackers/Hash-Buster.git")
            os.system("apt-get update -y")
            os.system("apt-get install -y git")
            os.system("apt-get install -y python2")
            os.system("cd && git clone https://github.com/shawarkhanethicalhacker/D-TECT.git")
            os.system("apt-get update -y")
            os.system("apt-get install -y git")
            os.system("apt-get install -y python2")
            os.system("cd && git clone https://github.com/reverse-shell/routersploit.git")
            os.system("cd && cd routersploit")
            os.system("pip2 install -r requirements.txt")
            os.system("pip2 install -r requirements-dev.txt")
            os.system("pip2 install -r requests")
            os.system("clear")
            print("========================================")
            print("[+] Всё было успешно установленно :)")
            print("[+] Счастливого хакинга <3")
            print("[+] Для выхода нажми \"Ctrl + Z\"")
            print("========================================")
            time.sleep(999)

        else:
            rmenu = input("[?] Вернутся в меню? (y/n): ")
            if rmenu == "y":
                menu()
            else:
                break
    if what == "1":
        os.system("cd")
        os.system("apt-get update -y")
        os.system("apt-get install -y nmap")
        os.system("sudo apt install nmap && cd")
        print("====================================")
        print("[+] nmap успешно установлен :)")
        print("[+] Введи 'nmap' для запуска.")
        print("====================================")
        rmenu = input("[?] Вернуться в меню? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "2":
        os.system("cd")
        os.system("apt-get update -y")
        os.system("apt-get install -y hydra")
        os.system("sudo apt install hydra && cd")
        print("====================================")
        print("[+] hydra успешно установленна :)")
        print("[+] Введи 'hydra' для запуска.")
        print("====================================")
        rmenu = input("[?] Вернуться в меню? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "3":
        os.system("cd")
        os.system("apt-get update -y")
        os.system("apt-get install -y git")
        os.system("apt-get install python2")
        os.system("cd && git clone https://github.com/sqlmapproject/sqlmap.git")
        os.system("sudo apt-get install sqlmap && cd")
        print("====================================")
        print("[+] SQLMap успешно установлен :)\n[+] Введи sqlmap для запуска.")
        print("====================================")
        rmenu = input("[?] Вернуться в меню? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "4":
        os.system("apt-get install -y wget")
        os.system("cd && wget https://Auxilus.github.io/metasploit.sh")
        os.system("cd && bash metasploit.sh")
        os.system("cd && cd metasploit-framework")
        os.system("cd && gem install bundle --pre")
        os.system("cd && bundle config build.nokogiri --use-system-libraries")
        os.system("cd && bundle install")
        os.system("cd")
        print("====================================")
        print("[+] Metasploit успешно установлен :)")
        print("====================================")
        rmenu = input("[?] Вернуться в меню? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "5":
        os.system("apt-get update -y")
        os.system("apt-get install -y git")
        os.system("cd && git clone https://github.com/themastersunil/ngrok.git")
        os.system("sudo snap install ngrok && cd")
        print("====================================")
        print("[+] ngrok успешно установлен :)")
        print("[+] Введи ngrok для запуска.")
        print("====================================")
        rmenu = input("[?] Вернуться в меню? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "6":
        os.system("apt-get update -y")
        os.system("cd && git clone https://github.com/Hax4us/Nethunter.git")
        os.system("cd && cd Nethunter && chmod +x kalinethunter")
        os.system("cd")
        print("====================================")
        print("[+] Nethunter не был установлен :)")
        print("====================================")
        rmenu = input("[?] Вернуться в меню? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "7":
        os.system("apt-get update -y")
        os.system("apt-get install -y git")
        os.system("apt-get install -y python2")
        os.system("cd && git clone https://github.com/ihebski/angryFuzzer.git")
        os.system("cd && cd angryFuzzer")
        os.system("cd && pip2 install -r requirements.txt")
        os.system("cd && pip2 install requests")
        os.system("cd")
        print("====================================")
        print("[+] angryFuzzer успешно установлен :)")
        print("[+] Открой angryFuzzer дирректорию и введи 'python2 angryFuzzer.py' для запуска.")
        print("====================================")
        rmenu = input("[?] Вернуться в меню? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "8":
        os.system("apt-get update -y")
        os.system("apt-get install -y git")
        os.system("apt-get install -y php")
        os.system("cd && git clone https://github.com/Tuhinshubhra/RED_HAWK")
        os.system("cd")
        print("====================================")
        print("[+] RED_HAWK успешно установлен :)")
        print("[+] Открой RED_HAWK дирректорию и введи 'php rhawk.php' для запуска.")
        print("====================================")
        rmenu = input("[?] Вернуться в меню? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "9":
        os.system("apt-get update -y")
        os.system("apt-get install -y python2")
        os.system("apt-get install -y git")
        os.system("cd && git clone https://github.com/evait-security/weeman.git")
        os.system("cd && cd weeman")
        os.system("cd && chmod +x weeman.py")
        os.system("cd")
        print("====================================")
        print("[+] weeman успешно установлен :)")
        print("[+] Открой weeman дирректорию и введи 'python2 weeman.py' для запуска.")
        print("====================================")
        rmenu = input("[?] Вернуться в меню? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "10":
        os.system("apt-get update -y")
        os.system("apt-get install -y git")
        os.system("apt-get install -y python")
        os.system("cd && git clone https://github.com/maldevel/IPGeoLocation.git")
        os.system("cd && cd IPGeoLocation")
        os.system("cd && pip install -r requirements.txt")
        os.system("cd")
        print("====================================")
        print("[+] IPGeoLocation успешно установлен :)")
        print("[+] Открой IPGeoLocation дирректорию и введи 'python ipgeolocation.py' для запуска.")
        print("====================================")
        rmenu = input("[?] Вернуться в меню? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "11":
        os.system("apt-get update -y")
        os.system("apt-get install -y git")
        os.system("apt-get install -y python")
        os.system("cd && git clone https://github.com/Mebus/cupp.git")
        print("====================================")
        print("[+] Cupp успешно установлен :)")
        print("[+] Открой cupp дирректорию и введи 'python cupp3.py' для запуска.")
        print("====================================")
        rmenu = input("[?] Вернуться в меню? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "12":
        os.system("apt-get update -y")
        os.system("apt-get install -y git")
        os.system("apt-get install -y python")
        os.system("apt-get install -y nano")
        os.system("pip install requests")
        os.system("pip install beautifulsoup4")
        os.system("cd && git clone https://github.com/avramit/instahack.git")
        print("====================================")
        print("[+] Instahack успешно установлен :)")
        print("====================================")
        rmenu = input("[?] Вернуться в меню? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "13":
        os.system("apt-get update -y")
        os.system("apt-get install -y git")
        os.system("apt-get install -y python")
        os.system("pip install mechanicalsoup")
        os.system("apt-get install -y nano")
        os.system("cd && git clone https://github.com/abdallahelsokary/TwitterSniper.git")
        print("====================================")
        print("[+] TwitterSniper успешно установлен :)")
        print("[+] Открой TwitterSniper дирректорию и введи 'python TwitterSniper.py' для запуска.")
        print("====================================")
        rmenu = input("[?] Вернуться в меню? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "14":
        os.system("apt-get update -y")
        os.system("apt-get install -y git")
        os.system("cd && git clone https://github.com/Neo-Oli/termux-ubuntu.git")
        os.system("cd && cd termux-ubuntu && bash ubuntu.sh")
        print("====================================")
        print("[+] Ubuntu успешно установлен :)")
        print("[+] Открой termux-ubuntu дирректорию и введи './start.sh' для запуска.")
        print("====================================")
        rmenu = input("[?] Вернуться в меню? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "15":
        os.system("apt-get update -y")
        os.system("apt-get install -y git")
        os.system("apt-get install -y wget")
        os.system("apt update && apt install wget -y && /data/data/com.termux/files/usr/bin/wget https://raw.githubusercontent.com/nmilosev/termux-fedora/master/termux-fedora.sh")
        print("====================================")
        print("[+] Fedora успешно установлен :)")
        print("====================================")
        rmenu = input("[?] Вернуться в меню? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "16":
        os.system("apt-get update -y")
        os.system("apt-get install -y git")
        os.system("apt-get install -y python2")
        os.system("cd && git clone https://github.com/blackvkng/viSQL.git && sudo pip install visql")
        print("====================================")
        print("[+] viSQL успешно установлен :)")
        print("[+] Введи visql для запуска.")
        print("====================================")
        rmenu = input("[?] Вернуться в меню? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "17":
        os.system("apt-get update -y")
        os.system("apt-get install -y git")
        os.system("apt-get install -y python2")
        os.system("cd && git clone https://github.com/UltimateHackers/Hash-Buster.git")
        print("====================================")
        print("[+] Hash-Buster успешно установлен :)")
        print("[+] Открой Hash-Buster дирректорию и введи 'python2 hash.py' для запуска.")
        print("====================================")
        rmenu = input("[?] Вернуться в меню? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "18":
        os.system("apt-get update -y")
        os.system("apt-get install -y git")
        os.system("apt-get install -y python2")
        os.system("cd && git clone https://github.com/shawarkhanethicalhacker/D-TECT.git")
        print("====================================")
        print("[+] D-TECT не был установлен :(")
        print("====================================")
        rmenu = input("[?] Вернуться в меню? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
            os.system("apt-get update -y")
            os.system("apt-get install -y git")
            os.system("apt-get install -y python2")
            os.system("cd && git clone https://github.com/reverse-shell/routersploit.git")
            os.system("cd && cd routersploit")
            os.system("pip2 install -r requirements.txt")
            os.system("pip2 install -r requirements-dev.txt")
            os.system("pip2 install -r requests")
            print("====================================")
            print("[+] routersploit успешно установлен :)")
            print("[+] Открой routersploit дирректорию и введи 'python2 rsf.py' для запуска.")
            print("====================================")
            rmenu = input("[?] Вернуться в меню? (y/n): ")
            if rmenu == "y":
                menu()
            else:
                break
    elif what == "99":
        print("Пока, юный хакер.")
        break

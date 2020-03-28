# -*- coding: utf-8 -*-
import os
import time
import getpass
import string
import smtplib as root
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from time import sleep
from colorama import Fore, Back, Style

#Автор - x11repo#
#При копипасте пожалуйста указывайте меня как Автора и не удаляйте эти строки
#!# Update 0.5 Beta #!#

os.system("cls")
os.system("clear")

def deleteModules(moduleName):
    del sys.modules["meenuuu"]
    del sys.modules["meenuuu.{}".format(moduleName)]

def main():
    def menu(selected = ""):
        os.system("cls")
        os.system("clear")

        if(selected == ""):
            from meenuuu import m0m0m0
            menu1 = input("$ > ")
            selected = menu1
        else:
            menu1 = selected

        print("SELECTED: " + selected)

        if selected == "7777":
            os.system("cd && rm -rf hack-tools && git clone https://github.com/x11-repo/hack-tools.git")
            print(Fore.BLUE+f"=====================================\n{Fore.GREEN}[INFO]{Style.RESET_ALL}Hack Tools \nбыл успешно обновлён.\n{Fore.GREEN}[INFO]{Style.RESET_ALL}Через 5 секунд он будет\n автоматически запущен\n{Fore.BLUE}====================================="+Style.RESET_ALL)
            time.sleep(5)
            os.system("cd && cd hack-tools && python3 HackTools.py")

        if selected == "999":

            from meenuuu import setup0
            print("========================================")
            print("[+] Всё было успешно установленно :)")
            print("[+] Счастливого хакинга <3")
            kkk = input("[+] Вернутся в меню? (y/n): ")
            print("========================================")
            if kkk == "y":
                menu()
                return

        if menu1 == "007":
            login = 'forbugsreport@yandex.ru'
            url = 'smtp.yandex.ru'
            toaddr = 'mail@x11repo.site'
            topic = 'Find bugs in HackTools.'
            asroote = 'server=post.root'
            message = input(Fore.RED+f'Введите ваше сообщение: ' )
            num = int('1')
            for value in range( num ):
                msg = MIMEMultipart()
                msg[ 'Subject' ] = topic
                msg[ 'From' ] = login
                body = message
                msg.attach( MIMEText( body, 'plain' ) )
                server = root.SMTP_SSL( url, 465 )
                server.login( login, asroote )
                server.sendmail( login, toaddr, msg.as_string() )
                value += 1
                print(Fore.GREEN+f'Письмо отправлено! Спасибо!'+Style.RESET_ALL)
                time.sleep(5)
                exit(0)

        if selected == "1":
            from meenuuu import m1m1m1
            deleteModules("m1m1m1")
            menu1 = input("$ > ")

        if menu1 == "011":
            os.system("sudo arp-scan")
            exit(0)
        if menu1 == "021":
            os.system("sudo cutycapt")
            exit(0)
        if menu1 == "031":
            os.system("sudo p0f")
            exit(0)
        if menu1 == "041":
            os.system("cd && cd sparta && chmod +x * && sudo python sparta.py")
            exit(0)
        if menu1 == "051":
            os.system("cd && cd golismero && chmod +x * && sudo python golismero.py")
            exit(0)
        if menu1 == "061":
            os.system("sudo masscan")
            exit(0)
        if menu1 == "071":
            os.system("cd && sudo java -jar ./jsql-injection-v*.jar")
            exit(0)

        if selected == "2":
            from meenuuu import m2m2m2
            deleteModules("m2m2m2")
            menu1 = input("$ > ")

        if menu1 == "012":
            os.system("sudo openvas-start")
            exit(0)

        if selected == "3":
            from meenuuu import m3m3m3
            deleteModules("m3m3m3")
            menu1 = input("$ > ")

        if menu1 == "013":
            os.system("cd && cd jboss-autopwn && sudo ./e2.sh")
            exit(0)
        if menu1 == "023":
            os.system("sudo dirb")
            exit(0)
        if menu1 == "033":
            os.system("sudo plecost")
            exit(0)
        if menu1 == "043":
            os.system("sudo wpscan")
            exit(0)
        if menu1 == "053":
            os.system("sudo xsser")
            exit(0)

        if selected == "4":
            from meenuuu import m4m4m4
            deleteModules("m4m4m4")
            menu1 = input("$ > ")

        if menu1 == "014":
            os.system("sudo crunch")
            exit(0)
        if menu1 == "024":
            os.system("cd && cd hack-tools/assets/hashcat/ && sudo ./hashcat64.bin --help")
            exit(0)
        if menu1 == "034":
            os.system("sudo john")
            exit(0)
        if menu1 == "044":
            os.system("sudo ncrack")
            exit(0)

        if selected == "5":
            from meenuuu import m5m5m5
            deleteModules("m5m5m5")
            menu1 = input("$ > ")

        if menu1 == "015":
            os.system("sudo aircrack-ng")
            exit(0)
        if menu1 == "025":
            os.system("cd && cd asleap-2.2 && sudo ./asleap")
            exit(0)
        if menu1 == "035":
            os.system("cd && cd cowpatty-4.6 && sudo ./cowpatty")
            exit(0)
        if menu1 == "045":
            os.system("sudo mdk3")
            exit(0)
        if menu1 == "055":
            os.system("sudo reaver")
            exit(0)
        if menu1 == "065":
            os.system("sudo wifite")
            exit(0)
        if menu1 == "075":
            os.system("cd && cd routersploit && sudo python3 rsf.py")
            exit(0)

        if selected == "6":
            from meenuuu import m6m6m6
            deleteModules("m6m6m6")
            menu1 = input("$ > ")

        if menu1 == "016":
            os.system("sudo yara")
            exit(0)

        if selected == "7":
            from meenuuu import m7m7m7
            deleteModules("m7m7m7")
            menu1 = input("$ > ")

        if menu1 == "017":
            print(" Скоро добавим. В данный момент недоступно")
            exit(0)
        if menu1 == "027":
            os.system("sudo setoolkit")
            exit(0)
        if menu1 == "037":
            os.system("cd && cd routersploit && sudo python3 rsf.py")
            exit(0)
        if menu1 == "047":
            os.system("sudo yersinia -h")
            exit(0)

        if selected == "8":
            from meenuuu import m8m8m8
            deleteModules("m8m8m8")
            menu1 = input("$ > ")

        if menu1 == "018":
            os.system("sudo ettercap -h")
            exit(0)
        if menu1 == "028":
            os.system("sudo sslstrip -h")
            exit(0)
        if menu1 == "038":
            os.system("sudo dsniff -h && sudo dnsiff -h && sudo dnssniff -h")
            exit(0)
        if menu1 == "048":
            os.system("sudo wireshark")
            exit(0)

        if selected == "9":
            from meenuuu import m9m9m9
            deleteModules("m9m9m9")
            menu1 = input("$ > ")

        if menu1 == "019":
            os.system("sudo dns2tcpd")
            exit(0)
        if menu1 == "029":
            os.system("sudo sbd")
            exit(0)
        if menu1 == "039":
            os.system("sudo nghttpd")
            exit(0)

        if selected == "10":
            from meenuuu import m10m10m10
            deleteModules("m10m10m10")
            menu1 = input("$ > ")

        if menu1 == "0110":
            os.system("sudo kdiff3")
            exit(0)
        if menu1 == "0210":
            os.system("sudo p0f")
            exit(0)
        if menu1 == "0310":
            os.system("sudo xpdf")
            exit(0)
        if menu1 == "0410":
            os.system("sudo exiftool")
            exit(0)

        if selected == "11":
            from meenuuu import m11m11m11
            deleteModules("m11m11m11")
            menu1 = input("$ > ")
        
        if menu1 == "0111":
            os.system("sudo cherrytree")
            exit(0)
        if menu1 == "0211":
            os.system("sudo xrdp -h")
            exit(0)
        if menu1 == "0311":
            os.system("sudo aircrack-ng --help")
            exit(0)
        if menu1 == "0411":
            os.system("sudo ardour5")
            exit(0)

        if selected == "12":
            from meenuuu import m12m12m12
            deleteModules("m12m12m12")
            menu1 = input("$ > ")

        if menu1 == "0112":
            os.system("sudo dhcpig")
            exit(0)
        if menu1 == "0212":
            os.system("sudo t50 -h")
            exit(0)
        if menu1 == "0312":
            os.system("sudo terminator")
            exit(0)
        if menu1 == "0412":
            os.system("sudo termineter")
            exit(0)

        if selected == "13":
            print("Еще не добавленно.")
            time.sleep(3)
            menu()

        if(not menu1.startswith("0")):
            # главные меню
            menu(menu1)
        else:
            # подменю
            time.sleep(1)
            menu(selected)   

        return

    menu()

main()

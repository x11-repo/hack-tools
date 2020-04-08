import os
import time
from colorama import Fore, Style, Back

print(Style.RESET_ALL+f"Введите основную ссылку домена, {Fore.GREEN}пример: https://example.com/")
link = input(Fore.RED+f"$ > {Fore.GREEN}")
os.system("wget -r -k -l 7 -p -E -nc " + link)
print(Fore.BLACK+f"{Back.WHITE}Процесс выгрузки был совершен. Если все прошло удачно, то в дирректории hack-tools/core или hack-tools/ была созданна папка с названием сайта, в которой вы найдете сам код."+Style.RESET_ALL)
exit(0)
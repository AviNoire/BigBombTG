import time
import colorama
from colorama import Fore
from termcolor import colored as color

print(color("""
                How to use?!
            {Coded by avinoire}
        {Dead_Lucifer\'s materials}""","red"))
time.sleep(0.5)
while True:
	time.sleep(0.1)
	print(f"""
{Fore.CYAN}[1] How to use?
{Fore.CYAN}[2] Authors
{Fore.RED}[3] Exit""")
	anv = input(f"""{Fore.RED}$ {Fore.CYAN}""")
	if anv == "2":
		time.sleep(0.7)
		print(f"""
			   {Fore.MAGENTA}A {Fore.GREEN}u {Fore.RED}T {Fore.CYAN}h {Fore.YELLOW}O {Fore.MAGENTA}r {Fore.RED}S {Fore.GREEN}""")
		print(color("""This programm was written by AviNoire. Material provided by Dead_Lucifer.
                         Check Telegramm by tags:
                         [Avinoire] - @avinoire
                         [Lucifer] - @Dead_Lucifer_666 ""","cyan"))
		time.sleep(1)
	elif anv == "1":
		time.sleep(0.7)
		print(f"""
{Fore.RED}Inscruction step by step.

{Fore.GREEN}1) start VPN

{Fore.GREEN}2) trigger bigbomb.py (bigbomb.py)

{Fore.GREEN}3) write your\'s bot token ( my should create it in @BotFather on Telegram ) and your Telegram id

{Fore.GREEN}4) go to your bot into Telegram and push Start

{Fore.GREEN}5) You will Menu on russian language

{Fore.GREEN}6) push \'Бомбер\'

{Fore.GREEN}7) Enter phone number

{Fore.GREEN}8) Relax""")
		time.sleep(1)
	elif anv == "3":
		break
	else:
		print(color("{---Unknown Command---}","red"))

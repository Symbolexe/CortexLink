# CortexLink Tool
# Creator  : Yasin Saffari ( Symbolexe )
# Github   : https://Github.com/Symbolexe/
# Telegram : https://T.Me/Symbolexe or https://T.Me/iPurpleTeam

from googlesearch import search 
from colorama import Fore
from os import system, name
if name == "nt":
    _ = system("cls")
else :
    _ = system("clear")
def banner():
    print(Fore.GREEN + """
░█████╗░░█████╗░██████╗░████████╗███████╗██╗░░██╗██╗░░░░░██╗███╗░░██╗██╗░░██╗
██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝╚██╗██╔╝██║░░░░░██║████╗░██║██║░██╔╝
██║░░╚═╝██║░░██║██████╔╝░░░██║░░░█████╗░░░╚███╔╝░██║░░░░░██║██╔██╗██║█████═╝░
██║░░██╗██║░░██║██╔══██╗░░░██║░░░██╔══╝░░░██╔██╗░██║░░░░░██║██║╚████║██╔═██╗░
╚█████╔╝╚█████╔╝██║░░██║░░░██║░░░███████╗██╔╝╚██╗███████╗██║██║░╚███║██║░╚██╗
░╚════╝░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚══════╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝
CortexLink is a search engine for searching about the topic you want.

Creator  : Yasin Saffari ( Symbolexe )
Github   : https://Github.com/Symbolexe/
Telegram : https://T.Me/symbolexe or https://T.Me/iPurpleTeam
          
Usage :
    Commands :
        exit      - Exit The Program
        me        - show your subscription & your system information
    Search Options :
        cve       - Go To Search about CVE Links
        exploit   - Go To Search about Exploit Links
        poc       - Go To Search about PoC Links
        learn     - Go To Search about Education & Learning Links
          """)
    print(Fore.YELLOW + """
*NOTE* : if you want to search about something, just type your word.\nEx : splunk 
""")
banner()
FINAL_TARGET = ""
USER_INPUT = str(input(Fore.GREEN + "[+] " + Fore.WHITE + "[Search Query]  : "))
if USER_INPUT == "me":
    import platform
    print(platform.machine())
    print(platform.version())
    print(platform.platform())
    print(platform.uname())
    print(platform.system())
    print(platform.processor())
    print(Fore.YELLOW + "[*] " + Fore.WHITE + "You're using free account.")
    input(Fore.GREEN + "[+] " + Fore.WHITE + "Press any key to close this page")
    exit(0)
elif USER_INPUT == "exit":
    exit(0)
TARGET = str(input(Fore.GREEN + "[+] " + Fore.WHITE + "[Search Option] : "))
print(Fore.YELLOW + "[*] " + Fore.WHITE + "For TLD, just type the name of TLD AND DO NOT USE DOT (.) , example : com / or another example is : org")
TLD_LIST = str(input(Fore.GREEN + "[+] "+ Fore.WHITE + "[TLD] : "))
if TARGET == "cve":
    FINAL_TARGET = USER_INPUT + TARGET + "list"
elif TARGET == "exploit":
    FINAL_TARGET = USER_INPUT + "exploits download"
elif TARGET == "learn":
    FINAL_TARGET = USER_INPUT + "crash course"
elif TARGET == "poc":
    FINAL_TARGET = USER_INPUT + "poc download"
else:
    exit(0)
QUERY = FINAL_TARGET
with open('Cortex-Link-Result.txt', 'w') as output:
    for RESULTS in search(QUERY, tld=TLD_LIST, num=100, stop=100, pause=2):
        output.write(RESULTS + "\n")
        print(RESULTS)
input(Fore.GREEN + "[+] " + Fore.WHITE + "Press any key to close this page")
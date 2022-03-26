import requests, json, sys, os
from colorama import Fore

green = Fore.GREEN
reset = Fore.RESET

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

print(f"""{green}
 ________                                                                         ______    __                          __
/        |                                                                       /      \  /  |                        /  |
$$$$$$$$/   _______   ______   _______    ______   _____  ____   __    __       /$$$$$$  |_$$ |_     ______    ______  $$ |  ______    ______
$$ |__     /       | /      \ /       \  /      \ /     \/    \ /  |  /  |      $$ \__$$// $$   |   /      \  /      \ $$ | /      \  /      \
$$    |   /$$$$$$$/ /$$$$$$  |$$$$$$$  |/$$$$$$  |$$$$$$ $$$$  |$$ |  $$ |      $$      \$$$$$$/   /$$$$$$  | $$$$$$  |$$ |/$$$$$$  |/$$$$$$  |
$$$$$/    $$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |       $$$$$$  | $$ | __ $$    $$ | /    $$ |$$ |$$    $$ |$$ |  $$/
$$ |_____ $$ \_____ $$ \__$$ |$$ |  $$ |$$ \__$$ |$$ | $$ | $$ |$$ \__$$ |      /  \__$$ | $$ |/  |$$$$$$$$/ /$$$$$$$ |$$ |$$$$$$$$/ $$ |
$$       |$$       |$$    $$/ $$ |  $$ |$$    $$/ $$ | $$ | $$ |$$    $$ |      $$    $$/  $$  $$/ $$       |$$    $$ |$$ |$$       |$$ |
$$$$$$$$/  $$$$$$$/  $$$$$$/  $$/   $$/  $$$$$$/  $$/  $$/  $$/  $$$$$$$ |       $$$$$$/    $$$$/   $$$$$$$/  $$$$$$$/ $$/  $$$$$$$/ $$/
                                                                /  \__$$ |
                                                                $$    $$/
                                                                 $$$$$$/
{reset}
""")

authorization = input(f'{green}Token: ')
prefix = input(f'{green}BOT Prefix: ')
channelId = input(f'{green}Channel ID: ')
userId = input(f'{green}User ID: ')
discordApiV = input(f'{green}[v9] API version: ')
url =  f"https://discord.com/api/{discordApiV}/channels/{channelId}/messages"
print(f"""{green}List of methods you can use:

1. collect
2. givemoney
3. withall
4. depall
{reset}""")
method = input(f'{green}method: ')

def sendmsg(content):
    headers={
        "authorization":f"{authorization}",
        "content-type": "application/json"
    }

    JsonPayload = {
        "content": content
    }
    r = requests.post(url=url, headers=headers, json=JsonPayload)
    print('-----------------------------------------------')
    print(r.text)
    print('-----------------------------------------------')
    print(f"{green}Have a nice day :){reset}")

if(method.lower()=='collect' or method.lower()=='1'):
    sendmsg(content=f"{prefix}collect")

elif(method.lower()=='givemoney' or method.lower()=='2'):
    sendmsg(content=f"{prefix}give <@{userId}> all")

elif(method.lower()=='withall' or method.lower()=='3'):
    sendmsg(content=f"{prefix}with all")

elif(method.lower()=='depall' or method.lower()=='4'):
    sendmsg(content=f"{prefix}dep all")

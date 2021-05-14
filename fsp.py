#Coding utf-8
#Import
import amino
import concurrent.futures
from colorama import init, Fore, Back, Style
init(autoreset=True)
print(Fore.LIGHTCYAN_EX + "Creator: obee\nsimple bot.")

#Account login
client = amino.Client()
def loginc():
    try:
        email = input(Fore.LIGHTGREEN_EX + "email - ")
        email2 = input(Fore.LIGHTGREEN_EX + "password - ")
        client.login(email, email2)
    except amino.exceptions.InvalidEmail:
        print(Fore.LIGHTRED_EX + "Invalid email")
    except amino.exceptions.InvalidPassword:
        print(Fore.LIGHTRED_EX + "Invalid password")
    except amino.exceptions.FailedLogin:
        print(Fore.LIGHTRED_EX + "Fail login")
    except amino.exceptions.ActionNotAllowed:
        print(Fore.LIGHTRED_EX + "Change deviceId")
    except: pass
loginc()

for name, id in zip(client.sub_clients().name, client.sub_clients().comId):
	print (name, id) 

wcm = input("comId - ")
print(Fore.LIGHTYELLOW_EX + "joined...")
subclient = amino.SubClient(comId=wcm, profile=client.profile)

userlink = input("link on user - ")
userlin = client.get_from_code(userlink).objectId
print(Fore.LIGHTYELLOW_EX + "Successfull")
def spam():
    subclient.follow(userId=userlin), subclient.unfollow(userId=userlin)
    
def sp():
    while True:
        with concurrent.futures.ThreadPoolExecutor(max_workers=2228) as executor:
            _ = [executor.submit(spam) for _ in range(5000000000000)]
            
def pupa():
    while True:
        with concurrent.futures.ThreadPoolExecutor(max_workers=2228) as executor:
            _ = [executor.submit(sp) for _ in range(5000000000000)]
            
pupa()
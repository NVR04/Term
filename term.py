import os
import fade, art
from colorama import Fore, init, Style
import time
import keyboard
import msvcrt


__mainAccent = f"{Fore.LIGHTBLUE_EX}"
__accent1 = f"{Fore.CYAN}"
__accent2 = f"{Fore.BLUE}"
__seperatorAccent = f"{Fore.WHITE}"

def printOptions(options:dict={"Test Option Without Info":"", "With Info":"Info"}, prompt:str=f"\n{__accent2}-->{__mainAccent} Choose{__seperatorAccent}:{__accent1} "):
    optionNum = 1
    for key in options:
        hasExtra = False
        option = options[key]
        if option != "": hasExtra = True

        if hasExtra: print(f"{__accent2}{optionNum}{__seperatorAccent}) {__mainAccent}{key}{__seperatorAccent}: {__accent1}{option}")
        else: print(f"{__accent2}{optionNum}{__seperatorAccent}) {__mainAccent}{key}{__seperatorAccent}")


        optionNum+=1


    if prompt != "":
        print(prompt, end="")
        return input()
def prompt(text:str=""):
    if text == "": print(f"\n{__accent2}-->{__mainAccent} Choose{__seperatorAccent}:{__accent1} ", end="")
    else: print(f"\n{__accent2}-->{__mainAccent} {text}{__seperatorAccent}:{__accent1} ", end="")
    return input()
def ask(text):
    def is_arrow_key(key):
        arrow_keys = [b'\xe0', b'\x00']
        return key in arrow_keys

    # Function to get the next arrow key pressed
    def get_key():
        while True:
            key = msvcrt.getch()
            if is_arrow_key(key):
                next_key = msvcrt.getch()
                return key + next_key
            elif is_enter_key(key):
                return key

    def is_enter_key(key):
        return key == b'\r'

    print(text)
    print(f"{__accent2}--> {Style.BRIGHT}{Fore.WHITE}>{__accent1}y{__accent2}\\{Style.NORMAL}{__mainAccent}n{__seperatorAccent}", end="\r")
    boolean = True
    while True:
        key = get_key()
        if key == b'\xe0K':
            print(f"{Style.NORMAL}{__accent2}--> {Style.BRIGHT}{Fore.WHITE}>{__accent1}y{__accent2}\\{Style.NORMAL}{__mainAccent}n{__seperatorAccent}", end="\r")
            boolean = True
        if key == b'\xe0M':
            print(f"{Style.NORMAL}{__accent2}--> {Fore.WHITE}{Style.NORMAL}{__mainAccent}{Style.BRIGHT}y{__accent2}\\{__accent1}n{__seperatorAccent}{Style.BRIGHT}{Fore.WHITE}<", end="\r")
            boolean = False
        if key == b'\r':
            time.sleep(0.3)
            return boolean


def cls(): os.system("cls" if os.name != 'posix' else quit())
def banner(text:str="NWRHook"):
    cls()
    print(fade.water(art.text2art(text)))
def alertG(text:str="NWRHook"):
    cls()
    print(fade.brazil(art.text2art(text)))
def alertR(text:str="NWRHook"):
    cls()
    print(fade.fire(art.text2art(text)))
def resizeTerm(X:int=120, Y:int=30):
    os.system(f"mode con:cols={X} lines={Y}")

init()


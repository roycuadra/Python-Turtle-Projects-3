# Diamond Structure using Numbers
import colorama
from colorama import Fore
colorama.init(autoreset=True)
s=Fore.RED+"* "
def diamond(num):
    for i in range(num):
        print(" "*(num-i-1)+s*(i+1))
    for j in range(num-1,0,-1):
        print(" "*(num-j)+s*(j))

a=int(input("Enter a number:"))
diamond(a)
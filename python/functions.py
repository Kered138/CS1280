import os
import time
import sys 

def clear():
    """
    Clears Console
    """
    # Clear console
    os.system('cls' if os.name == 'nt' else 'clear')

def printOld(word,delay = 0.05):
    """
    Takes a string a displays it with a delay in between each character and 
    Args:
    word :: string to print
    delay :: optional custom delay, default is 0.05
    """
    for char in word:
        print(char, end='',flush=True)
        time.sleep(delay)  
    print()

def inputOld(word,delay = 0.05):
    """
    Takes a string a displays it with a delay in between each character and returns user input
    Args:
    word :: string to print
    delay :: optional custom delay, default is 0.05
    """
    for char in word:
        print(char,end='',flush=True)
        time.sleep(delay)
    return input()  
    
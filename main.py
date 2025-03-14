import sys

from functions.startMessage import startMessage
from functions.printRules import printRules

print("Welcome to the Blackjack!")
while True:
    startMessage()
    answer = input("Waiting for input: ")
    if answer == "quit":
        sys.exit("Thanks for playing!")
    elif answer == "rules":
        printRules()

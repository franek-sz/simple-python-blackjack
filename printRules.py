def printRules():
    while True:
        print("1. Card Values")
        print("2. Payouts")
        print("3. Dealer")
        print("Type 'exit' to go back to the main menu.")
        print('########################################')
        rule = str(input("What do you want to know about: (eg. type '1' to get card values) "))
        if rule == "1":
            print("Card Values")
            print("A = 1 or 11. Q, K, J = 10, Rest equal their respective numbers.")
            print("---------------------------------------------------------------")
        elif rule == "2":
            print("Payouts:")
            print("Blackjack pays 3 to 2, Insurance pays 2 to 1.")
            print("---------------------------------------------")
        elif rule == "3":
            print("Dealer:")
            print("Dealer must draw to 16 and stand on 17.")
            print("---------------------------------------")
        elif rule == "exit":
            return 0
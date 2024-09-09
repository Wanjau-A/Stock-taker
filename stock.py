def main():
    choices= input("STOCK INTAKE \nSTOCK AVAILABLE \nNEEDED STOCK? \n").capitalize()
    for choice in choices:
        if choice == "STOCK INTAKE":
            return stock_intake()
        elif choice == "STOCK AVAILABLE":
            return stock_onboard()
        elif choice == "NEEDED STOCK":
            return depleted()
        else:
            print("INVALID INPUT!")

def stock_intake():
    stock = []
    connect = input("NAME: NUMBER")
    connect.append()
    print(stock)

def stock_onboard():
    input()
def depleted():
    input()


if __name__ == "__main__":
    main()

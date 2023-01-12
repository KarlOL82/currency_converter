def main():
    print("This program converts USD to Pounds Sterling")
    print("")

    dollars = eval(input("Enter amount in USD: "))

    pounds = convert_to_pounds(dollars)

    print("That is", pounds, "Pounds.")

convert_to_pounds = lambda dollars: dollars * 0.82

main()
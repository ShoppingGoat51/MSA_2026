def get_data(prompt, max):
    while True:
        try:
            data = float(input(f"Enter the {prompt}: "))
            if data <= 0:
                print("ERROR: Enter a number between 0 and 24.")
                continue
            if max == True and data > 24:
                print("ERROR: Enter a number between 0 and 24.")
                continue
            return data
        except:
            print("ERROR: Please enter a number.")
            continue

def main():
    hours = get_data("number of hours worked daily", True)
    wage = get_data("hourly wage", False)
    gross_income = 260 * hours * wage
    taxes = .12 * gross_income
    net_income = gross_income - taxes

    print("\nPay Advice\n-------------")
    print(f"Hours Worked: {hours:.2f}")
    print(f"Hourly Wage: ${wage:,.2f}")
    print(f"Wages Before Taxes: ${gross_income:,.2f}")
    print(f"Tax Amount: ${taxes:,.2f}")
    print(f"Annual Wage After Taxes: ${net_income:,.2f}\n")

main()
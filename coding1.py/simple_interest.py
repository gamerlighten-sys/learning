money_lent = float(input("enter money lent: $"))
time = float(input("enter number of years: "))
rate = float(input("enter rate of interest: "))

(SI) = (money_lent * rate * time) / 100
amount_payable = SI + money_lent

print(f"the amount payable is: {amount_payable}")
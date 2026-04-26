# money_lent = float(input("enter money lent: $"))
# time = float(input("enter number of years: "))
# rate = float(input("enter rate of interest: "))

# amount_payable = money_lent * (1 + rate / 100) * time
# compound_interest = amount_payable - money_lent

# print(f"the amount payable is: {compound_interest}")



money_lent = float(input("enter money lent: $"))
time = float(input("enter number of years: "))
rate = float(input("enter rate of interest: "))

amount_payable = money_lent * (1 + rate / 100) ** time
compound_interest = amount_payable - money_lent
rounded = round(compound_interest, 2)

print(f"the compund interest is: {rounded}")
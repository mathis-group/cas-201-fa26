
balance = 1000
rate = 0.10
years = 18

def compound(balance, rate):
    return (1.0 + rate)*balance

for i in range(1, years+1):
            print(f"In the {i} year, the balance is {balance:.2f}")
            balance =    compound(balance, rate)

print(f"The balance value is: {balance:.2f}")
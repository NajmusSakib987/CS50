amount = 50

while amount > 0:
    print(f'Amount Due: {amount}')
    coin = int(input("Insert Coin: "))
    #the machine takes only 5,10,25 cents
    if coin in [5,10,25]:

        amount -= coin

print(f'Change Owed: {abs(amount)}')



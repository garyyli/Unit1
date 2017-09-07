#Gary Li
#9/7/17
#change.py

cents = int(input('Input a number of cents: '))
quarters = cents//25
print('Quarters:', quarters)

coinsAfterQuarters = cents%25
dimes = coinsAfterQuarters//10
print('Dimes:', dimes)

coinsAfterDimes = coinsAfterQuarters%10
nickels = coinsAfterDimes//5
print('Nickels:', nickels)

coinsAfterNickels = coinsAfterDimes%5
pennies = coinsAfterNickels//1
print('Pennies:', pennies)
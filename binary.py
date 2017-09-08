#Gary Li
#9/8/17
#binary.py

binary = int(input('Enter an 8-digit binary number: '))
first = binary%10
second = first%10
third = second%10
fourth = third%10
fifth = fourth%10
sixth = fifth%10
seventh = sixth%10
eighth = seventh%10

print((first*(2**0))+(second*(2**1))+(third*(2**2))+(fourth*(2**3))+(fifth*(2**4))+(sixth*(2**5))+(seventh*(2**6))+(eighth*(2**7)))
bin(binary)
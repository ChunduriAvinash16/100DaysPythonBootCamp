# Write your code below this line 👇
import math


def prime_checker(number):
    isPrime = True
    if number == 2:
        isPrime = True
    else:
        for i in range(2,math.sqrt(number)+1):
            if number%i == 0:
                isPrime = False
    if isPrime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

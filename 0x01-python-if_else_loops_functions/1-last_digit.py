#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_dig = abs(number) % 10
if number < 0:
    last_dig *= -1
print(f"Last digit of {number} is {last_dig} and is", end=" ")
if last_dig == 0:
    print("0")
elif 6 > last_dig != 0:
    print("less than 6 and not 0")
elif last_dig > 5:
    print("greater than 5")

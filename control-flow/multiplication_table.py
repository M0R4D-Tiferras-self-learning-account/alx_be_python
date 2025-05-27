#!/usr/bin/python3

num = int(input("Enter a number to see its multiplication table: "))

for it in range(1, 11):
    result = num * it
    print(f"{num} * {it} = {result}")
#!/usr/bin/python3

num = int(input("Enter a number to see its multiplication table: "))

for it in range(11):
    if (it > 0):
        print(f"{num} * {it} = {num * it}")
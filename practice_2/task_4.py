# -*- coding: utf-8 -*-
"""
Develop a program that asks the user for an integer 4-digit number 
and calculates the sum of its constituent digits. 
For example, if the user enters the number 3141, 
the program should output the following result:
3 + 1 + 4 + 1 = 9

"""

def sum_of_digits():
    try:
        user_input = input("Enter a 4-digit number:\n")
        if not user_input.isdigit() or len(user_input) != 4:
            raise ValueError("Your input must be a 4-digit number.")
    except ValueError as ve:
        print(f"Error: {ve}")
    else:
        a, b, c, d = user_input
        resulting_sum = sum(int(x) for x in user_input)
        answer = f"{a} + {b} + {c} + {d} = {resulting_sum}"
        print(answer)

sum_of_digits()
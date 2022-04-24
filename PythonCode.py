import re
import string
import random

shopping_list = []


def printsomething():
    print("Hello from python!")

def PrintMe(v):
    print("You sent me: " + v)
    return 100;

def SquareValue(v):
    return v * v

def SortList():
    cleaned_list = []
    product_count = {}
    with open('input.txt', 'r') as f:
        for lines in f.readlines():
            cleaned_list.append(lines.strip())
    f.close()
    print("-------------------------------------------------")

    for item in cleaned_list:
        counter = cleaned_list.count(item)
        if item in product_count:
            continue
        else:
            product_count[item] = counter
    print("-------------------------------------------------")

    for product in product_count:
        print("{} has sold {} times.".format(product, product_count[product]))
    print("-------------------------------------------------")

def SortByName():
    cleaned_list = []
    product_count = {}
    with open('input.txt', 'r') as f:
        for lines in f.readlines():
            cleaned_list.append(lines.strip())
    f.close()
    print("-------------------------------------------------")

    for item in cleaned_list:
        counter = cleaned_list.count(item)
        if item in product_count:
            continue
        else:
            product_count[item] = counter
    print("-------------------------------------------------")

    print("Enter product:")
    user_input = input()
    if user_input in product_count:
        print("{} has sold {} times.".format(user_input, product_count[user_input]))
    else:
        print("Try again")
    print("-------------------------------------------------")
    
def PrintHistogram():
    cleaned_list = []
    product_count = {}
    with open('input.txt', 'r') as f:
        for lines in f.readlines():
            cleaned_list.append(lines.strip())
    f.close()
    print("-------------------------------------------------")

    for item in cleaned_list:
        counter = cleaned_list.count(item)
        if item in product_count:
            continue
        else:
            product_count[item] = counter
    print("-------------------------------------------------")
    
    for x in product_count:
        print(x)
        print("\t +" * product_count[x])
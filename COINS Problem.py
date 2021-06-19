# I'm writing as an exercise for don't foget my programming
# skills, the exercises came from web site clalled codechefe
# https://www.codechef.com/problems/COINS
from math import floor


def enter_your_bytecoin_value():
    opc = 1
    while opc != 0:
        bytecoin_amount = int(input("Type your Bytelandian amount of money:"))

        print(conversion(bytecoin_amount))

        opc = int(input("Type 0 exit the program or other thing to convert to other coin."))

def conversion(bytecoin_amount):
    result = 0
    result += floor(bytecoin_amount / 2)
    result += floor(bytecoin_amount / 3)
    result += floor(bytecoin_amount / 4)

    if(result < bytecoin_amount):
        return bytecoin_amount

    return result

enter_your_bytecoin_value()

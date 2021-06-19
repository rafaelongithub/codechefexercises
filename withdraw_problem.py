# This is problem from code chefe web site
# https://www.codechef.com/problems/HS08TEST

account_amount = 2000.00

# check if withdraw amount valid
def is_valid(withdraw_amount):
    if(withdraw_amount > (account_amount + 0.50)):
        return False
    if (withdraw_amount % 5) == 0:
        return True
    else:
        return False


finishe = 2

while finishe != 1:
    withdraw_amount = float(input("Type the amount that you want withdraw:"))
    if(is_valid(withdraw_amount)):
        account_amount = account_amount - (withdraw_amount + 0.50)
    else:
     print("You have not typed a valid value to withdraw.")

    print(account_amount)
    finishe = int(input("Type 1 to finishe the program.\nOr type other thing to cotinue."))

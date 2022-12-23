#Project 2: Change Maker

from curses.ascii import isalpha
from os import CLD_CONTINUED


print("Welcome to the vending machine change maker program")
print("Change maker initialized.")

#initializing stock
nickels = 25
dimes = 25
quarters = 25
ones = 0
fives = 0

#printing the contents of the stock
print(f"Stock contains:\n   {nickels} nickels\n   {dimes} dimes\n   {quarters} quarters\n   {ones} ones\n   {fives} fives\n")

user_input = 0

#prompting user for a price in the form xx.xx, where x denotes a digit, or to enter 'q' to quit
while user_input != 'q':
    user_input = input("Enter the purchase price (xx.xx) or `q' to quit: ")

    if user_input != 'q':
        if '.' in user_input:
            user_input_list = user_input.split('.')
        elif user_input.isdigit == True:
            user_input_float = float(user_input)
            purchase_price = int(round(user_input_float * 100))
        elif len(user_input) == 2 and str(user_input).isdigit() == True:
            user_input_float = float(user_input)
            purchase_price = int(round(user_input_float * 100))
        else:
            print("Invalid purchase price. Try again")
            continue

        if '.' in user_input and user_input.find('.') == 2:
            if user_input_list[0].isdigit() == True and user_input_list[1].isdigit() == True:
                user_input_float = float(user_input)
                purchase_price = int(round(user_input_float * 100))
            else:
                print("Invalid purchase price. Try again")
                continue
        elif '.' in user_input and user_input.find('.') == 0:
            if user_input_list[1].isdigit() == True:
                user_input_float = float(user_input)
                purchase_price = int(round(user_input_float * 100))
            else:
                print('Invalid purchase price. Try again')
                continue
        elif '.' in user_input and user_input.find('.') == 1:
            if user_input_list[0].isdigit() == True and user_input_list[1].isdigit() == True:
                user_input_float = float(user_input)
                purchase_price = int(round(user_input_float * 100))
            else:
                print("Invalid purchase price. Try again")
                continue

        user_input_float = float(user_input)
        purchase_price = int(round(user_input_float, 2) * 100)

        #checking price is a multiple of .05
        if purchase_price % 5 != 0:
            #printing error message and starting over requesting either a new price or to quit
            print("")
            print("Illegal price: Must be a non-negative multiple of 5 cents. \n")
            continue
        else:
            #printing menu for indicating coin/bill deposited or to cancel payment
            print("")
            print("")
            print("Menu for deposits:")
            print("  'n' - deposit a nickel\n  'd' - deposit a dime\n  'q' - deposit a quarter\n  'o' - deposit a one dollar bill\n  'f' - deposit a five dollar bill\n  'c' - cancel the purchase\n")

            dollars = int(purchase_price // 100)
            cents = int(purchase_price % 100)

            #printing put the payment due
            if dollars > 0:
                print(f"Payment due: {dollars} dollars and {cents} cents")
            else:
                print(f"Payment due: {cents} cents")

            payment = 0
            deposited_nickels = 0
            deposited_dimes = 0
            deposited_quarters = 0
            deposited_ones = 0
            deposited_fives = 0
            payment_due = 0
            due = purchase_price

            while payment < purchase_price:
                #prompting for a selection from the menu
                deposit = input("Indicate your deposit: ")

                if deposit == 'n':
                    nickels += 1
                    deposited_nickels += 1
                    payment += 5
                    due -= 5
                elif deposit == 'd':
                    dimes += 1
                    deposited_dimes += 1
                    payment += 10
                    due -= 10
                elif deposit == 'q':
                    quarters += 1
                    deposited_quarters += 1
                    payment += 25 #change to a variable
                    due -= 25
                elif deposit == 'o':
                    ones += 1
                    deposited_ones += 1
                    payment += 100
                    due -= 100
                elif deposit == 'f':
                    fives += 1
                    deposited_fives += 1
                    payment += 500
                    due -= 500
                elif deposit == 'c': 
                    print("")
                    print("")
                    print("Please take the change below.")
                    quarter_owed = 0
                    dime_owed = 0
                    nickel_owed = 0

                    
                    while payment > 0:
                        if payment >= 25 and quarters > 0:
                            max_quarter_owed = payment // 25
                            if quarters >= max_quarter_owed:
                                quarter_owed = max_quarter_owed
                                print(f"   {quarter_owed} quarters")
                                quarters -= max_quarter_owed
                                payment -= max_quarter_owed * 25
                                continue
                            else:
                                quarter_owed = quarters
                                print(f"   {quarter_owed} quarters")
                                quarters = 0
                                payment -= quarter_owed * 25
                                continue
                        elif payment >= 10 and dimes > 0:
                            max_dime_owed = payment // 10
                            if dimes >= max_dime_owed:
                                dime_owed = max_dime_owed
                                print(f"   {dime_owed} dimes")
                                dimes -= max_dime_owed
                                payment -= max_dime_owed * 10
                                continue
                            else:
                                dime_owed = dimes
                                print(f"   {dime_owed} dimes")
                                dimes = 0
                                payment -= dime_owed * 10
                                continue
                        elif payment >= 5 and nickels > 0:
                            max_nickel_owed = payment // 5
                            if nickels >= max_nickel_owed:
                                nickel_owed = max_nickel_owed
                                print(f"   {nickel_owed} nickels")
                                nickels -= max_nickel_owed
                                payment -= max_nickel_owed * 5
                            else:
                                nickel_owed = nickels
                                print(f"   {nickel_owed} nickels")
                                nickels = 0
                                payment -= nickel_owed * 5

                        if payment > 0:
                            print("")
                            print("Machine is out of change.")
                            print("See store manager for remaining refund.")
                            print("")
                            amount_due_d = payment // 100
                            amount_due_c = payment % 100
                            print(f"Amount due is: {amount_due_d} dollars and {amount_due_c} cents")
                            break

                    print(f"Stock contains:\n   {nickels} nickels\n   {dimes} dimes\n   {quarters} quarters\n   {ones} ones\n   {fives} fives\n")
                    break
            

                else:
                    print("")
                    print(f"Illegal selection: {deposit}")

                if purchase_price > payment and deposit != 'c':
                    due_dollars = due // 100
                    due_cents = due % 100
                    print("")
                    if due_dollars > 0:
                        print(f"Payment due: {due_dollars} dollars and {due_cents} cents")
                    else:
                        print(f"Payment due: {due_cents} cents")

            change_fives = 0
            change_ones = 0
            change_quarters = 0
            change_dimes = 0
            change_nickels = 0

            #determining no. of coins to be dispensed in change or as a refund
            if purchase_price < payment and deposit != 'c': 
                print("")
                print("")
                print("Please take the change below.")

                change = payment - purchase_price

                while change > 0:

                    if change >= 25 and quarters > 0:
                        max_change_quarters = change // 25
                        if max_change_quarters <= quarters:
                            change_quarters = max_change_quarters
                            print(f"    {change_quarters} quarters")
                            change -= change_quarters * 25
                            quarters -= change_quarters
                            continue
                        else:
                            change_quarters = quarters
                            print(f"    {change_quarters} quarters")
                            change -= change_quarters * 25
                            quarters = 0
                            continue

                    elif change >= 10 and dimes > 0:
                        max_change_dimes = change // 10
                        if max_change_dimes <= dimes:
                            change_dimes = max_change_dimes
                            print(f"    {change_dimes} dimes")
                            change -= change_dimes * 10
                            dimes -= change_dimes
                            continue
                        else:
                            change_dimes = dimes
                            print(f"    {change_dimes} dimes")
                            change -= change_dimes * 10
                            dimes = 0
                            continue

                    elif change >= 5 and nickels > 0:
                        max_change_nickels = change // 5
                        if max_change_nickels <= nickels:
                            change_nickels = max_change_nickels
                            print(f"    {change_nickels} nickels")
                            change -= change_nickels * 5
                            nickels -= change_nickels
                        else:
                            change_nickels = nickels
                            print(f"    {change_nickels} nickels")
                            change -= change_nickels * 5
                            nickels = 0

                    if change > 0:
                            print("Machine is out of change.")
                            print("See store manager for remaining refund.")
                            amount_due_d = change // 100
                            amount_due_c = change % 100
                            print(f"Amount due is: {amount_due_d} dollars and {amount_due_c} cents")
                            break

                #printing the total amount left in the stock
                print("Stock contains: ")
                print(f"   {nickels} nickels\n   {dimes} dimes\n   {quarters} quarters\n   {ones} ones\n   {fives} fives\n")
            elif payment == purchase_price and deposit != 'c':
                print("")
                print("")
                print("Please take the change below.")
                print("  No change due.")
                #printing the total amount left in the stock
                print("Stock contains: ")
                print(f"   {nickels} nickels\n   {dimes} dimes\n   {quarters} quarters\n   {ones} ones\n   {fives} fives\n")
            else:
                continue

if user_input == 'q':
    total = (nickels * 5) + (dimes * 10) + (quarters * 25) + (ones * 100) + (fives * 500)
    total_dollars = total // 100
    total_cents = total % 100
    print("")
    print(f"Total: {total_dollars} dollars and {total_cents} cents")
    
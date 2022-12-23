# UMass Fall 2022 Info90S - Project 2 Change Maker

** Overview **

This project will give you more experience on the use of:
  integers (int)
  floats (float)
  strings (str)
  branching
  loops
Your program will simulate a simple change maker for a vending machine. It will start with a stock of coins and dollars. It will then repeatedly request the price for an item to be purchased or to quit. If given a price, it will accept nickels, dimes, quarters, one-dollar and five-dollar bills, deposited one at a time, in payment.  When the user has deposited enough to cover the cost of the item, the program will calculate the coins to be dispensed in change.  Alternatively, the user can cancel the purchase up until full payment has been deposited, in which case, your program will calculate the coins to be dispensed to refund any partial payment already deposited. With each purchase, the program will update the stock of coins and dollars.  Before quitting, it will output the remaining stock of coins and dollars. The specifications are spelled out more thoroughly below. An example interaction with our program appears at the end of this description. All change and refunds must be in coins only, and must use the minimum number of coins possible.


** Project Specification **

General
- You must implement your solution in a single python file named change_maker.py. If you do not name your program file correctly, you will not receive credit.
- At program start, assume a stock of 25 nickels, 25 dimes, and 25 quarters.  Print the contents of the stock.
- Repeatedly prompt the user for a price in the form xx.xx, where x denotes a digit, or to enter ‘q’ to quit.
Just before quitting, print the total amount (the number of dollars and number of cents) left in the stock.

When a Price is Entered
- Check that the price entered is a (non-negative) multiple of .05 (i.e., it is payable in nickels).  If not, then print an error message and start over requesting either a new price or to quit (indicated by entering a ‘q’).
- Print a menu for indicating the coin/bill deposited or to cancel payment.
- Prompt for a selection from this menu.
- If the user enters an illegal selection, re-prompt for a correct one.
- Following each deposit, print the remaining amount owed (indicate the number of dollars and the number of cents).
- When full payment has been deposited or a ‘c’ has been entered, determine the coins to be dispensed in change or as a refund. This calculation will depend on the amount to be dispensed and also on the number of coins left in the stock. For example, the least number of coins needed to make up $1.30 is 6 (5 quarters and 1 nickel).  But if there are only 3 quarters, 3 dimes, and 10 nickels left in the stock, then the least number is 11 (3 quarters, 3 dimes, and 5 nickels).
- Print the numbers of the coins to be dispensed and their denominations. (Omit a denomination if no coins of that denomination will be dispensed.)
- In the case where an exact payment is deposited, print a message such as “No change.” 
- If the change cannot be made up with the coins remaining, dispense the coins available without exceeding the change amount and indicate the amount still due to the user, which will have to be collected from a store manager. For example, if the stock contains one nickel, no dimes, and a quarter and if the change amount is 15 cents, dispense just the nickel and indicate the user should collect 10 cents from a store manager. 
- Print the contents of the stock following the transaction.

Exceeding
- To achieve a grade in the A range for this project you must satisfy the following requirements:
- Check that the purchase price entered is formatted properly as a xx.xx floating-point value, where each x is a digit. If the price is not formatted properly, then print an error message and start over requesting either a new print or to quit.

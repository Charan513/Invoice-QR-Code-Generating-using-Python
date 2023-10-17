
# Package or Library

import pyqrcode

# code

total_amount = 0
next_line = "\n"

header="                         Invoice Details                   \n"
# header = "                Invoice Details                \n"
client_name = input("Enter client name: ")
invoice_date = input("Enter Invoice Date: ")
due_date = input("Enter Due Date: ")
invoice_number = input("Enter Invoice number: ")
po_number = input("Enter PO number: ")
print("Enter Item Description:")

item_description = ""
for i in range(1, 6):
    description = input(str(i) + ". ")              # Type conversion --> int (i) into string (i). And Append dot after string.
    quantity = int(input("Enter Quantity: "))       # Quantity in int.
    amount = int(input("Enter Amount: "))           # Amount in int.
    print()

    item_description += f"{description} - {quantity} - {amount},"    # Assign values to empty variable. Using Format string --> place holder{}  Quantity: Amount: 
    total_amount += amount

print("Total Amount: $", total_amount)              # Optional command for me 

QR_Name = input("Enter QR Code name with serial No: ")

string = header + next_line + "Client Name : " + client_name + next_line \
        + "Invoice Date : " + invoice_date + next_line \
        + "Due Date : " + due_date + next_line \
        + "Invoice Number : " + invoice_number + next_line \
        + "PO Number : " + po_number + next_line \
        + "Item Description :\n"

item_description = item_description.rstrip(", ")  # Remove the trailing comma and space

string += item_description + next_line + "Total Amount : $" + str(total_amount) + next_line + next_line + "Payment Mode : Paypal"

QR_code = pyqrcode.create(string)
QR_code.svg(QR_Name + ".svg", scale=4)
# QR_code.png(QR_Name + ".png", scale=4)
total_bill = float(input("Enter the bill amount to be paid:"))
amount_paid = float(input("Enter the amount paid by the customer:"))
if amount_paid > total_bill:
    due_amount = amount_paid - total_bill
    print("Due amount to be paid:", due_amount)
elif total_bill > amount_paid:
    due_amount = total_bill - amount_paid 
    print("Due amount to be paid:", due_amount)
else:
    print("Amount fully paid")
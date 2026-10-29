cp = float(input("Enter cost price of the book: "))
discount = float(input("Enter discount percentage: "))

discount_amount = (cp * discount) / 100
sp = cp - discount_amount

print("Selling price of the book =", sp)

feet = float(input("Enter distance in feet: "))
inches = float(input("Enter distance in inches: "))

total_inches = (feet * 12) + inches
total_cm = total_inches * 2.54
meters = total_cm / 100

print("Distance in meters =", meters)
print("Distance in centimeters =", total_cm)

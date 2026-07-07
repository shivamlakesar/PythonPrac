km = int(input("Enter distance in km: "))

if km <= 3:
    charge = 40

elif km <= 5:
    charge = 40 + (km - 3) * 5

elif km <= 10:
    charge = 40 + (2 * 5) + (km - 5) * 3

elif km <= 15:
    charge = 40 + (2 * 5) + (5 * 3) + (km - 10) * 2

else:
    print("Delivery not available")
    exit()

print(f"Delivery Charge = ₹{charge}")

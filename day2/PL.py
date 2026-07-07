#1: enter sale price and cost price of a product and print profit or loss

cp = float(input("Enter Cost Price: "))
sp = float(input("Enter SElling Price: "))

if sp > cp:
    profit = sp - cp
    print(f"profit = {profit}")

elif sp < cp:
    loss = cp - sp
    print(f"loss= {loss}")

else :
    print("No profit or loss")

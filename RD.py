'''
17. enter premium amount of rd and print maturity amount 
Rule:
1. RD open for 5 years
2. minimum amount of rd premium inr 5/- per month 
3. max no limit but 5*?
standard rule: inr 5/- premium per month for 5 years = maturity 340.27
10/- 680.54
'''
premium = float(input("Enter Monthly Premium: "))

maturity = premium * 68.054

print("maturity amount :",maturity)
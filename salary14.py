#14. enter basic salary of employee , calculate hra=10% of basic, da=55% of basic, pf=12% of basic and print gross salary
   # grosssalary=basic+hra+da-pf

basic = float(input("Enter Basic Salary: "))

hra = basic * 10 / 100
da = basic * 55 / 100
pf = basic * 12 / 100

gross = basic + hra + da - pf

print(f"HRA = {hra}")
print(f"DA = {da}")
print(f"PF = {pf}")
print(f"Gross Salary = {gross}")
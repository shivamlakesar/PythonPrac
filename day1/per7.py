#enter marks of 5 subjects and print total and percentage

s1 = float(input("Enter marks of Subject 1: "))
s2 = float(input("Enter marks of Subject 2: "))
s3 = float(input("Enter marks of Subject 3: "))
s4 = float(input("Enter marks of Subject 4: "))
s5 = float(input("Enter marks of Subject 5: "))

total = s1 + s2 + s3 + s4 + s5
percentage = total / 5

print(f"Total Marks = {total}")
print(f"Percentage = {percentage}%")
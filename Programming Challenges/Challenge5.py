from datetime import datetime

dob = input("Enter your date of birth (DD/MM/YYY): ")
currentdate = datetime.today().strftime("%d/%m/%Y")

d1 = datetime.strptime(dob, "%d/%m/%Y")
d2 = datetime.strptime(currentdate, "%d/%m/%Y")

difference = d2 - d1
print(f'Difference is {difference.days} days')
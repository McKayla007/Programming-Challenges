from datetime import date

year = int(input("Enter your year of birth: "))
month = int(input("Enter your month of birth: "))
day = int(input("Enter your day of birth: "))

currentyear = int(date.today().strftime("%Y"))
currentmonth = int(date.today().strftime("%m"))
currentday = int(date.today().strftime("%d"))

def leapyear(year, currentyear):
    for i in range(year, currentyear, 4):
        leapyr=+1
        print(leapyr)

def birthdaythisyear(month, day, currentmonth, currentday):
    if currentmonth > month:
        return True
    elif currentmonth == month and currentday == day: 
        return "Today"
    else:
        return False
    
birthdayyet = birthdaythisyear(month, day, currentmonth, currentday)
if birthdayyet == "Today":
    daysalive = (currentyear - year) * 365

daysalive = (currentyear-year)*365
print("You have lived",)
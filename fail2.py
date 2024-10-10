from datetime import date

year = int(input("Enter your year of birth: "))
month = int(input("Enter your month of birth: "))
day = int(input("Enter your day of birth: "))

currentyear = int(date.today().strftime("%Y"))
currentmonth = int(date.today().strftime("%m"))
currentday = int(date.today().strftime("%d"))

leapyears = [2024, 2020, 2016, 2012, 2008, 2004, 2000]

def isleapyear(currentyear, year):
    for leapyear in leapyears:
        if currentyear == leapyear:
            print(1)
            return True

isitaleapyear = isleapyear(currentyear, year)

def howmanyleapyears(currentyear, year):
    temp = currentyear - year
    if isitaleapyear:
        temp = int(temp / 4 )
        print(temp)
        return temp
    
leapyearcount = howmanyleapyears(currentyear, year)

def isitpastleapday(currentmonth, currentday):
    if isitaleapyear and currentday == 29 and currentmonth == 2:
        return True
    elif isitaleapyear and currentmonth > 2:
        return True
    
pastleapday = isitpastleapday(currentmonth, currentday)


def birthmonthvalue(month):
    match month:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
           monthvalue = 31
           return monthvalue
        case 4 | 6 | 9 | 11:
            monthvalue = 30
            return monthvalue
        case 2:
            if isitaleapyear:
                monthvalue = 29
            else:
                monthvalue = 28
            return monthvalue
        
def currentmonthvalue(currentmonth):
    match currentmonth:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
           monthvalue = 31
           return monthvalue
        case 4 | 6 | 9 | 11:
            monthvalue = 30
            return monthvalue
        case 2:
            if isitaleapyear:
                monthvalue = 29
            else:
                monthvalue = 28
            return monthvalue
        
birthdaymonthvalue = birthmonthvalue(month)
todaysmonthvalue = currentmonthvalue(currentmonth)
print(birthdaymonthvalue)
print(todaysmonthvalue)

def birthdayyet(currentmonth, month):
    if currentmonth > month:
        return "Month past"
    elif currentmonth == month and currentday == day:
        return "Today"
    elif currentmonth == month and currentday >= day:
        return "Day past"
    elif currentmonth == month and currentday < day:
        return "Days early"
    elif currentmonth < month:
        return "Month early"

haveuhadurbirthday = birthdayyet(currentmonth, month)

if haveuhadurbirthday == "Today" and isitaleapyear and pastleapday:
    daysalive = 365 * (currentyear - year) + leapyearcount + 1
    print("You have been living for", daysalive,"days")

elif haveuhadurbirthday == "Today":
    daysalive = 365 * (currentyear - year) + leapyearcount
    print("You have been living for", daysalive,"days")


# elif haveuhadurbirthday == "Today":
  #  daysalive = 365 * (currentyear - year) + leapyearcount
  #  print("You have been living for", daysalive,"days")


elif haveuhadurbirthday == "Day past" and isitaleapyear and pastleapday:
    temp = currentday - day
    daysalive = 365 * (currentyear - year) + leapyearcount + temp + 1
    print("You have been living for", daysalive,"days")

elif haveuhadurbirthday == "Day past":
    temp = currentday - day
    daysalive = 365 * (currentyear - year) + leapyearcount + temp
    print("You have been living for", daysalive,"days")

elif haveuhadurbirthday == "Days early" and isitaleapyear and pastleapday:
    temp = currentday - day
    daysalive = 365 * (currentyear - year) + leapyearcount + temp + 1
    print("You have been living for", daysalive,"days")

elif haveuhadurbirthday == "Days early":
    temp = currentday - day
    daysalive = 365 * (currentyear - year) + leapyearcount + temp
    print("You have been living for", daysalive,"days")

elif haveuhadurbirthday == "Month early":
    temp = currentday - day
    temp2 = currentmonth - month
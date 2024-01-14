months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")
    if "/" in date:
        month,day,year = date.split('/')
        try:
            month,day,year = map(int, (month,day,year))
        except ValueError:
            continue
        
        else:    
            if month > 12 or day > 31:
                continue
            print(f"{year}-{month:02}-{day:02}")
            break
    elif "," in date:
        month_day,year = date.split(',')
        month,day = month_day.split(" ")
        try:
            day = int(day)
            year = int(year.strip())
        except ValueError:
            continue
        else:
            if day > 31 or (not month in months):
                continue
            print(f"{year}-{int(months.index(month)+1):02}-{day:02}")
            break
    else:
        continue

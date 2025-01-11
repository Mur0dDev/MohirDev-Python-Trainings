while True:

    investment = input("Enter Investment: $") # initial investment
    percentage = input("Enter Percentage: ") # the percentage that increased by day
    days = input("Enter Period in days: ") # the trading period in days
    n = 1
    indicator = []
    msg = f"You have entered wrong input!!! \nYou have to Enter number for"
    
    if not investment.isdigit():
        indicator.append(1)
        msg += " Investment: "
    if not percentage.isdigit():
        indicator.append(1)
        msg += " Percentage: "
    if not days.isdigit():
        indicator.append(1)
        msg += " Days: "
        
    if 1 in indicator:
        print(msg)
        print()
    else:
        investment = int(investment)
        percentage = int(percentage)
        days = int(days)
        while n <= days:
            n += 1
            investment += (investment/100)*percentage

        print(investment)
        print()
        
        yn = input("Wanna calculate one more time? (y/n): ")
        if yn == "n":
            break
        else:
            print("You may use again :)")
   
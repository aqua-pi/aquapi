import os, pause
from datetime import datetime

def updateTips():
    messages = ["outlet,message\n"]
    bad_usage = []
    amazing_usage = []
    rising_usage = []
    lowering_usage = []
    for file in os.listdir(os.fsencode("rates/daily")):
        outlet = os.fsdecode(file).replace(".csv", "")
        now = datetime.datetime.now()
        with open("totals/daily.csv", 'r') as file:
            data = file.readlines()
            line_number = [index for index, item in enumerate(data) if (outlet + ",") in item]
            daily_value = float(data[line_number[0]])
        with open("totals/weekly.csv", 'r') as file:
            data = file.readlines()
            line_number = [index for index, item in enumerate(data) if (outlet + ",") in item]
            weekly_value = float(data[line_number[0]]) / 7
        with open("totals/monthly.csv", 'r') as file:
            data = file.readlines()
            line_number = [index for index, item in enumerate(data) if (outlet + ",") in item]
            monthly_value = float(data[line_number[0]]) / 30
        if (weekly_value < monthly_value):
            if (daily_value < monthly_value):
                message = "Great improvement - keep doing what you're doing!"
                if outlet != "global":
                    amazing_usage.append(outlet)
            else:
                message = "Water usage is rising again - try to reduce your usage slightly."
                if outlet != "global":
                    rising_usage.append(outlet)
        elif (daily_value < weekly_value):
            message = "Water usage is improving - well done."
            if outlet != "global":
                lowering_usage.append(outlet)
        else:
            message = "Water usage is high, and is increasing - try to lower it."
            if outlet != "global":
                bad_usage.append(outlet)
        messages.extend((outlet + "," + message + ""))
    improvement_outlets = []
    if (len(bad_usage) > 0):
        improvement = "Drastically improve usage at "
        for outlet in bad_usage:
            improvement_outlets.append(outlet.lower())
    elif (len(rising_usage) > 0):
        improvement = "Improve usage at "
        for outlet in rising_usage:
            improvement_outlets.append(outlet.lower())
    else:
        improvement = "Your water usage is decreasing - keep up the good work!"
    
    improvement += "{}, and {}".format(", ".join(improvement_outlets[:-1]), improvement_outlets[-1])
    
    # update file
    with open("improvement-messages.csv", 'w') as file:
        file.writelines(messages)
        
    # update file
    with open("global-improvement.txt", 'w') as file:
        file.writelines(improvement)

# update AI tips every 24 hours
while True:
    today = datetime.today()
    pause.until(datetime(today.year, today.month, today.day, 0, 0, 0))
    updateTips()
    with open("totals/daily.csv", 'r') as file:
        file.write("outlet,total\n")
    with open("totals/daily/global.csv", 'r') as file:
        file.write("outlet,total\n")
    with open("totals/daily/Bath.csv", 'r') as file:
        file.write("outlet,total\n")
    if (today.weekday() == 0):
        with open("totals/weekly.csv", 'r') as file:
            file.write("outlet,total\n")
        with open("totals/weekly/global.csv", 'r') as file:
            file.write("outlet,total\n")
        with open("totals/weekly/Bath.csv", 'r') as file:
            file.write("outlet,total\n")
    if (today.day() == 1):
        with open("totals/monthly.csv", 'r') as file:
            file.write("outlet,total\n")
        with open("totals/monthly/global.csv", 'r') as file:
            file.write("outlet,total\n")
        with open("totals/monthly/Bath.csv", 'r') as file:
            file.write("outlet,total\n")
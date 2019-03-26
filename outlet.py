import datetime, time
import RPi.GPIO as GPIO
outlet_name = "Bath"

def updateOutletRates(filepath):
    data_value = rate
    
    with open(filepath, 'a+') as file:
        file.write(str(datetime.datetime.now().replace(microsecond=0)) + "," + data_value + "\r\n")

def updateGlobalRates():
    with open(filepath, 'r') as file:
        data = file.readlines()
    
    print(data)
    
    line_number = [index for index, item in enumerate(data) if (outlet_name + ",") in item]
    data_value = rate
    new_data_value = float(data[line_number[0]].replace(outlet_name + ",", "")) + float(data_value)
    
    # change data value
    data[line_number[0]] = str(datetime.datetime.now().replace(microsecond=0)) + "," + str(new_data_value) + "\n"
    
    # update file
    with open(filepath, 'w') as file:
        file.writelines(data)

def updateGlobalTotals():
    with open('totals/global.csv', 'r') as file:
        data = file.readlines()
    
    print(data)
    
    line_number = [index for index, item in enumerate(data) if (outlet_name + ",") in item]
    data_value = rate / 60
    new_data_value = float(data[line_number[0]].replace(outlet_name + ",", "")) + float(data_value)
    
    # change data value
    data[line_number[0]] = outlet_name + "," + str(new_data_value) + "\n"
    
    # update file
    with open('totals/global.csv', 'w') as file:
        file.writelines(data)

# setup GPIO input from flowmeter
def hall_pulse(channel):
    global pulse_count
    pulse_count += 1

global pulse_count = 0
global rate
GPIO.setmode(GPIO.BCM)
GPIO.setup(8, GPIO.IN, pull_up_down = GPIO.PUD_UP) # pin 8

GPIO.add_event_detect(8, GPIO.FALLING, callback=hall_pulse, bouncetime=50)

# update files every second
start_time = time.time()
while True:
    rate = pulse_count / 7.5 # litres per minute
    pulse_count = 0
    updateOutletRates("rates/daily/" + outlet_name + ".csv")
    updateOutletRates("rates/weekly/" + outlet_name + ".csv")
    updateOutletRates("rates/monthly/" + outlet_name + ".csv")
    updateGlobalRates("rates/daily/global.csv")
    updateGlobalRates("rates/weekly/global.csv")
    updateGlobalRates("rates/monthly/global.csv")
    updateGlobalTotals("totals/daily/global.csv")
    updateGlobalTotals("totals/weekly/global.csv")
    updateGlobalTotals("totals/monthly/global.csv")
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))
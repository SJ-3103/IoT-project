import RPi.GPIO as GPIO
from Adafruit_DHT import read_retry, DHT11
from csv_writter import makearow

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# GPIO PIN 4
def temperature_fun(row_list):
    humidity, temperature = read_retry(DHT11, 4)
    temperature = int(temperature)
    humidity = int(humidity)
    print("[VALUE] Temperature: {} C, Humidity: {} %".format(temperature,humidity))
    
    if temperature in range(20,34) and humidity in range(35,75):
        print("[MSG] The weather is alright.")
    else:
        print("[MSG] The temperature and Humidity are not suitable.")

    makearow(temperature, row_list)
    makearow(humidity, row_list)

    return row_list

# print(temperature_fun([]))
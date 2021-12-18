import time
from Adafruit_DHT import read_retry, DHT11
from main import makearow


# GPIO PIN 4
def temperature(row_list):
    humidity, temperature = read_retry(DHT11, 4)
    print("[VALUE] Temperature: {0:0.1f} C, Humidity: {0:0.1f} %".format(temperature,humidity))
    
    if temperature in range(20,34) and humidity in range(35,75):
        print("[MSG] The weather is alright.")
    else:
        print("[MSG] The temperature and Humidity are not suitable.")
    
    temperature = int(temperature)
    humidity = int(humidity)
    
    makearow(temperature, row_list)
    makearow(humidity, row_list)
    
    return row_list

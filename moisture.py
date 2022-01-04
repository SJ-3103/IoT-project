from csv_writter import makearow
from main import blink
from gpiozero import DigitalInputDevice

digital_input = DigitalInputDevice(17)

def moisture(row_list):
    if not digital_input.value:
        print("Moisture level in soil has reached its threshold")
        plant_water_msg = False
    else:
        print("You need to water your plant.")
        blink(5,"red")
        plant_water_msg = True

    makearow(plant_water_msg,row_list)
    return row_list
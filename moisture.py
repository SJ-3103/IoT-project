from main import blink
from gpiozero import DigitalInputDevice

digital_input = DigitalInputDevice(17)

# def moisture(row_list):
#     print("[VAL] Moisture reading: {}" .format(moistval))
    
#     if moistval >= 930:
#         print("[INFO] No Water, Can you please Water me")
#         blink(5, "blue")
#     elif moistval <= 930 and moistval >= 500:
#         print("[MSG] Need some water")
#     elif moistval <= 500 and moistval >= 325:
#         print("[MSG] I'm doing good now")
#     elif moistval <= 325:
#         print("[MSG] Can you stop over pouring me please, I'm filled totally")
#     moistval= int(moistval)
#     makearow(moistval, row_list)
#     return row_list

# moisture([])

print(digital_input.value)
# import time
# while True:
#     if (not digital_input.value):
#         print('Moisture threshold reached!!!')
#     else:
#         print('You need to water your plant')
#         time.sleep(2)
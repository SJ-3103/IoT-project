from time import sleep
import Adafruit_MCP3008 as mcp
from csv_writter import makearow
from blink import blink

mcpval = mcp.MCP3008(clk=11, cs=8, miso=9, mosi=10)    # Setting MCP3008


def light(row_list):
    lightval = mcpval.read_adc(1)   # at channel 1
    print("[VAL] Light readings: {}" .format(lightval))
    
    if lightval == 1023:
        print("[MSG] The light is alright")
    else:
        print("[MSG] Light is insufficient")
    
    makearow(lightval, row_list)
    sleep(2)
    return row_list


def moisture(row_list):
    moistval = mcpval.read_adc(0)
    print("[VAL] Moisture reading: {}" .format(moistval))
    
    if moistval >= 930:
        print("[INFO] No Water, Can you please Water me")
        blink(5, "blue")
    elif moistval <= 930 and moistval >= 500:
        print("[MSG] Need some water")
    elif moistval <= 500 and moistval >= 325:
        print("[MSG] I'm doing good now")
    elif moistval <= 325:
        print("[MSG] Can you stop over pouring me please, I'm filled totally")
    moistval= int(moistval)
    makearow(moistval, row_list)
    return row_list

moisture([])
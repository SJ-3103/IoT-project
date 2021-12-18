import Adafruit_MCP3008 as mcp

from main import makearow
from main import blink


mcpval = mcp.MCP3008(clk=11, cs=8, miso=9, mosi=10)    # Setting MCP3008

def light(row_list):
    lightval = mcpval.read_adc(1)
    print("[VAL] Light readings: {}" .format(lightval))
    
    if lightval == 0:
        print("[MSG] Light is insufficient")
    else:
        print("[MSG] The light is alright")
    
    makearow(lightval, row_list)
    return row_list


def moisture(row_list):
    moistval = mcpval.read_adc(0)    # Reading moisture value
    print("[VAL] Moisture reading: {}" .format(moistval))
    # code to determine the status of water
    if moistval >= 930:
        print("[INFO] No Water, Can you please Water me")
        blink(5, "green")
    elif moistval <= 930 and moistval >= 500:
        print("[MSG] Need some water")
    elif moistval <= 500 and moistval >= 325:
        print("[MSG] I'm doing good now")
    elif moistval <= 325:
        print("[MSG] Can you stop over pouring me please, I'm filled totally")
    moistval= int(moistval)
    makearow(moistval, row_list)
    return row_list
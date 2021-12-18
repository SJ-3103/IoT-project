import RPi.GPIO as GPIO

from time import sleep,time,ctime
from csv import writer

from mail.main import sendmail
from temperature.main import temperature
from mcp.main import light,moisture
from motion.main import motion


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(12, GPIO.OUT)    # Setup the red LED 
GPIO.setup(18, GPIO.OUT)    # Setup the green LED

starttime = time()

def blink(n, color):
    GPIO.output(12,GPIO.LOW)
    GPIO.output(18,GPIO.LOW)
    if color == "green":
        pin = 18
    elif color == "red":
        pin = 12
    for b in range(n):
        GPIO.output(pin,GPIO.HIGH)
        sleep(0.2)
        GPIO.output(pin,GPIO.LOW)
        sleep(0.2)


def append_csv(file_name, list_of_elem):
    
    with open(file_name, 'a') as write_obj:
        csv_writer = writer(write_obj)      # Create a writer object from csv module
        csv_writer.writerow(list_of_elem)       # Add contents of list as last row in the csv file
    
    print("[INFO] Row Updated \n[MSG] File name: {}" .format(file_name))


def makearow(item_val, row_list):
    row_list.append(item_val)
    return row_list


def sendreport():
    file_name1 = "my_database.csv"
    subject = "Updated Report {}" .format(file_name1)
    path_name = "/home/pi/groot/mspy/{}" .format(file_name1)
    body_message = " Check the attachment below for detailed logs \n File Name: Report {}" .format(file_name1)
    sendmail(subject, file_name1, path_name, body_message)


def main():
    blink(1, "red")
    print("[INFO] Program Run Time {} seconds" .format(round(time() - starttime)))
    upcount = 1
    while True:
        row_list = []
        
        if round(time() - starttime) % 30 <= 1.5:    # run this code for every 30 seconds time interval
            print("\n[{}][INFO] Reading Values..." .format(upcount))
            print("[INFO] Check Run Time {} seconds" .format(round(time() - starttime)))  # Set the time delay for the check
            timestamp1=ctime().replace(" ","_").replace(":","-")
            
            makearow(timestamp1, row_list)     # Makes the first column ie for date and time
           
            temperature(row_list)     # Reads the temperature value and loads into the list named 'row_list'
            light(row_list)    # Reads the light sensitivity and saves into the list named 'row_list'
            moisture(row_list)    # Reads the moisture value and saves into the list named 'row_list'
            
            csv_file = "my_database.csv"    # The target csv file
            
            append_csv(csv_file, row_list)    # Appends the 'row_list' to the csv file
            
            upcount =+ 1
            print("[INFO] Motion Detection Running...\t" )
        elif round(time() - starttime) % 3600 <= 1.5:
            print("Email function is called here!")            
        else:
            motion()

        sleep(2.5)

if __name__ == "__main__":
    main()
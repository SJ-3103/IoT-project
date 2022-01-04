import RPi.GPIO as GPIO
from time import sleep,time,ctime
from mail import sendmail
from temperature import temperature_fun
from moisture import moisture
from motion import motion
from csv_writter import makearow,append_csv

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(12, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

starttime = time()

def blink(n, color):
    GPIO.output(12,GPIO.LOW)
    GPIO.output(18,GPIO.LOW)
    if color == "red":
        pin = 12
    elif color == "green":
        pin = 18
    for b in range(n):
        GPIO.output(pin,GPIO.HIGH)
        sleep(0.1)
        GPIO.output(pin,GPIO.LOW)
        sleep(0.1)



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
            
            makearow(timestamp1, row_list)     # Makes the first column i.e for date and time
            temperature_fun(row_list)     # Reads the temperature value and loads into the list named 'row_list'
            # light(row_list)    # Reads the light sensitivity and saves into the list named 'row_list'
            moisture(row_list)    # Checks the moisture value and saves message into the list named 'row_list'
            
            csv_file = "my_database.csv"    # The target csv file
            append_csv(csv_file, row_list)    # Appends the 'row_list' to the csv file
            
            upcount =+ 1
            print("[INFO] Motion Detection Running...\t" )
        
        elif round(time() - starttime) % 3600 <= 1.5:
            subject = "Regular Plant Update."
            file_name = "my_database.csv"
            path_name = "/home/pi/Desktop/IoT-project/{}".format(file_name)
            body_message = "Below are the regular updates containing the various parameters."
            sendmail(subject,file_name,path_name,body_message)

        else:
            motion()
        sleep(2.5)

if __name__ == "__main__":
    main()

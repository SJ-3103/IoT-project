import RPi.GPIO as GPIO
from time import sleep,time,ctime
from mail import sendmail
from temperature import temperature_fun
from moisture import moisture
from motion import motion
from csv_writter import makearow,append_csv
from blink import blink
starttime = time()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

def main():
    blink(1, "red")
    print("[INFO] Program Run Time {} seconds" .format(round(time() - starttime)))
    upcount = 1
    while True:
        row_list = []
        if round(time() - starttime) % 30 <= 1:    # run this code for every 30 seconds time interval
            print("\n[{}][INFO] Reading Values..." .format(upcount))
            print("[INFO] Check Run Time {} seconds" .format(round(time() - starttime)))  # Set the time delay for the check
            timestamp1=ctime().replace(" ","_").replace(":","-")
            
            makearow(timestamp1, row_list)     # Makes the first column i.e for date and time
            temperature_fun(row_list)     # Reads the temperature value and loads into the list named 'row_list'
            # light(row_list)    # Reads the light sensitivity and saves into the list named 'row_list'
            moisture(row_list)    # Checks the moisture value and saves message into the list named 'row_list'
            
            csv_file = "my_database.csv"    # The target csv file
            append_csv(csv_file, row_list)    # Appends the 'row_list' to the csv file
            
            upcount = upcount + 1
            print("[INFO] Motion Detection Running...\t" )
        
            subject = "Regular Plant Update."
            file_name = "my_database.csv"
            path_name = "/home/pi/Desktop/IoT-project/{}".format(file_name)
            body_message = "Below are the regular updates containing the various parameters."
            print("-------------------------\n[MSG]Email sent to user.")
            sendmail(subject,file_name,path_name,body_message)

        else:
            motion()
            sleep(30)

main()

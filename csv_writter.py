from mail import sendmail
from csv import writer

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

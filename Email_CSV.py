# Importing the necessary packages
import csv
import smtplib
import getpass

# Defining the sendEmail() with i_emailid and i_password as arguments
def sendEmail(i_emailid, i_password):
    # Create a smtp session
    smtp = smtplib.SMTP('smtp.gmail.com', 587)

    # Starting TLS for security
    smtp.starttls()

    # Authenticate the user
    smtp.login(i_emailid, i_password)

    # Printing success message
    print("\nLOGGED-IN SUCCESSFULLY")

    # Specifying the name of the CSV File
    csvFILE = "Usernames_Email-ID.csv"

    # Initializing the csvFIELDS and csvVALUES list
    csvVALUES = []

    # Opening the above mentioned CSV File in the read mode. File object is named as csv_file
    with open(csvFILE, 'r') as csv_file:
        # Creating an object of the csv.reader() named csvREADER_Obj and
        # converting file object to the csv.reader() object
        csvREADER_Obj = csv.reader(csv_file)

        # Skipping the CSV Header (Column Names - USERNAMES, EMAIL ID).
        # IF COLUMN NAMES ARE NOT USED, COMMENT OR DELETE THIS BELOW LINE OF CODE
        next(csvREADER_Obj)

        # Fetch values from the rows of the CSV File one by one and add it to the csvVALUES[]
        for row in csvREADER_Obj:
            csvVALUES.append(row)

        # Iterating through each value in csvVALUES list and sending the email to the
        # Email-ID contained in the csvVALUES list
        for value in csvVALUES:
            # Creating a message with user's name from csvVALUES[] and saving in message variable
            # User's names are the first value (Index 0) from csvVALUES list
            message = "Hey.. Good Day "+value[0]+"."

            # Sending the email to the Email-ID in the csvVALUES list with the above mesage
            # Email-Ids are the second value (Index 1) from csvVALUES list
            smtp.sendmail(i_emailid, value[1], message)
            # Syntax - smtp.sendmail(sender's-id, receiver's-id, message)

            # Printing the success message
            print("\nMESSAGE SENT TO "+ value[0])

        # Terminating the session
        smtp.quit()

# Driver Code
if __name__ == '__main__':
    # Prompting the user to enter Email-ID and Password to login
    emailid = input("\nENTER YOUR EMAIL-ID : ")
    password = getpass.getpass("ENTER YOUR PASSWORD : ")

    # Calling the sendEmail() with emailid and password as arguments
    sendEmail(emailid, password)

import datetime
import os
import reports
import emails

# return paragraph which will be added to pdf file
def readFruitFiles():
    fruit_description_path = "supplier-data/descriptions/"
    paragraph = ""
    for file in os.listdir(fruit_description_path):
        with open((fruit_description_path + file), 'r') as fruit_file:
            file_data = fruit_file.readlines()
        item_name_and_weight = "name: {}<br/>weight: {}<br/><br/>".format(file_data[0], file_data[1])
        paragraph += item_name_and_weight
    return paragraph

# print(readFruitFiles())
if __name__ == "__main__":
    #   fruit_data_list = readFruitFiles()
    #   print(fruit_data_list)
    # format current date
      present_date = datetime.datetime.now()
      present_date = present_date.strftime("%b %d, %Y")
      
      attachment = './processed.pdf'
      title = 'Processed Update on {}<br/>'.format(present_date)
      paragraph = readFruitFiles() # assign name and weight
      
    #   print(attachment)
    #   print(title)
    #   print(paragraph)
      
      # Generate PDF file
      reports.generate_report(attachment, title, paragraph)
      
      
      sender = "automation@example.com"
      recipient = "username@example.com"
      subject = "Upload Completed - Online Fruit Store"
      body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
      attachment_path = attachment # pdf file path
      
      # Make email and send it
      email_message = emails.generate_email(sender, recipient, subject, body, attachment_path)
      emails.send_email(email_message)

    
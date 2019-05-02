# email sender

import yagmail

def send_email(sender,sender_pass, receiver, email_subject, contents_array):
    yag = yagmail.SMTP(sender, sender_pass)
    yag.send(to=receiver, subject=email_subject, contents=contents_array)




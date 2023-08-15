import smtplib
def mailSend(receiver,subject,mail_content,mailfrom):
    from email.message import EmailMessage
    receiver=receiver.strip()
    mailfrom=mailfrom.strip()

    # The mail addresses and password
    sender_address = 'mailer.vns123@gmail.com'
    sender_pass = 'mailer@123'
    receiver_address = receiver
    # Setup the MIME
    msg = EmailMessage()
    msg.add_header('Content-Type', 'text/html')
    mail_content=mail_content.encode('utf-8')
    msg.set_payload(mail_content)

    #msg.set_content(mail_content)
    msg['Subject'] = subject
    msg['From'] = mailfrom
    msg['To'] = receiver

    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
    session.starttls()  # enable security
    session.login('mailer.vns123@gmail.com', sender_pass)  # login with mail_id and password
    session.send_message(msg)
    session.quit()
    print('Mail Sent to ', receiver)
# mailSend("coolshubhamroy@gmail.com","Testing my Mailer","Hi SHubham, where is Shivank?","Joe Biden")
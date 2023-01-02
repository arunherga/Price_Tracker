import smtplib
def send_main():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('bhatarunherga@gmail.com','niwfbtjikbwwfinf')
    server.sendmail('bhatarunherga@gmail.com',('arun.b.bhat@gmail.com'),'hi python is sending mail')
    print("mail sent")
send_main()
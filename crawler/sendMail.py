import smtplib


server = smtplib.SMTP('localhost:25')
server.sendmail('Me <my_account@gmail.com'>, ['to_user@gmail.com'], 'Hi!'.as_string())
server.quit()
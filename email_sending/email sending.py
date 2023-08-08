import smtplib as s

ob = s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()

user_name = '' #Enter your emiail ID
password = '' #Enter your password
ob.login(user_name, password)

subject = "testing"
body = 'hello'
message = f'subject: {subject}\n body: {body}'
add_list = ['guneet1206kaur@gmail.com','guneet.anand2323@gmail.com']

ob.sendmail('guneet1206kaur@gmail.com', add_list, message)
print("sent")
ob.quit()

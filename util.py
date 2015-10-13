def mail(to,text,court,date,count):
	import smtplib
	from email.mime.multipart import MIMEMultipart
	from email.mime.text import MIMEText
	msg = MIMEMultipart('alternative')	
	msg['Subject'] = court+"  "+str(date)
	a=str(text)
	part2 = MIMEText(a, 'html')
	msg.attach(part2)
	s=smtplib.SMTP_SSL()
	s.connect("smtp.gmail.com",465)
	s.login("user@gmail.com", "userpassword")
	#Works with gmail account of the user. Will have to change the connectivity for other mail options
	s.sendmail("user@gmail.com",str(to), msg.as_string())
	count=1
	return count
	s.quit()

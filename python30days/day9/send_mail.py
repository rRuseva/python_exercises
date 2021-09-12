import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

username = 'ruseva.radina.ru@gmail.com'
password = 'dw96bh66'


def send_mail(text="Email Body", subject='Hello World', from_email='Radina Ruseva <ruseva.radina.ru@gmail.com>', to_emails=None, html=None):

	### rise an error if 'to_emails' is NOT a list type
	assert isinstance(to_emails, list)

	msg = MIMEMultipart('alternative')
	msg['From'] = from_email
	
	msg['To'] = ", ".join(to_emails)
	msg['Subject'] = subject

	txt_part = MIMEText(text, 'plain')
	msg.attach(txt_part)
	
	if html != None:
		html_part = MIMEText(html, 'html')
		msg.attach(html_part)

	msg_str = msg.as_string()

    ### login to stmp server
	server = smtplib.SMTP(host='smtp.gmail.com', port=587)
	server.ehlo()
	server.starttls()
	server.login(username, password)
	server.sendmail(from_email, to_emails, msg_str)
	server.quit()



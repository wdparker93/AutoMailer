#Automatic clip-board messaging using pyperclip

#! python3
# autoMail.py - Loops through a dictionary of subjects and bodies for emails and automatically sends them to a specified recipient

#Must register your username and password,
#download keyring (pip install --upgrade keyring),
#download yagmail (pip install yagmail),
#and configure Google security settings to allow app logins from less secure apps.
#Register username/password with yagmail.register('address@gmail.com', 'password')

phrases = {'subject1': 'body1',
        'subject2': 'body2',
        'subject3': 'body3'}

import sys, yagmail

if len(sys.argv) < 2:
    print('Usage: python autoMail.py [NumLoops]')
    sys.exit()

numLoops = int(sys.argv[1])     #the number of emails to send

yag = yagmail.SMTP('sender@gmail.com')
recipient = 'recipient@gmail.com'

for i in range(numLoops):
    for k, v in phrases.items():
        theSubject=k
        theBody=v
        yag.send(
            to=recipient,
            subject=theSubject,
            contents=theBody,
        )


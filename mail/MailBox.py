import email
import getpass
import imaplib
import re

class MailBox:

    def getPattern(self, emailId):
        session = []
        for eId in emailId:
            response, data = self.m.fetch(eId, "RFC822") #'RFC822' means all mail data
            email_body = data[0][1]
            mail = email.message_from_string(email_body)
            lines = mail.get_payload().split('\r\n') #extract line
            session += [l for l in lines if re.match("Arr*", l)]
        return session


    def getMailFrom(self, author):
        self.m.select("INBOX")
        response, items = self.m.search(None, '(FROM "' + author + '")') # return 'OK' and 'id1 id2 ...'
        return items[0].split() #split string id of matching mail


    def __init__(self, user):
        self.user = user
        self.pwd = getpass.getpass('pwd: ')
#        try:
        self.m = imaplib.IMAP4_SSL("imap.gmail.com") # connecting to the gmail imap server
        self.m.login(self.user, self.pwd)
#        except IMAP4.error:

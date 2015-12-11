import email
import getpass
import imaplib
import re

class MailBox:
    """
    mailbox interaction with imap protocol
    """

    def getPattern(self, emailId):
        session = []
        for eId in emailId:
            response, data = self.m.fetch(eId, "RFC822")        #'RFC822' means all mail data
            email_body = data[0][1]
            mail = email.message_from_string(email_body)
            lines = mail.get_payload().split('\r\n')        #extract line
            session += [l for l in lines if re.match("Arr*", l)]
        print 'get {0} matching lines'.format(str(len(session)))
        return session


    def getMailFrom(self, author):
        self.m.select("INBOX")
        response, items = self.m.search(None, '(FROM "' + author + '")')        # return 'OK' and 'id1 id2 ...'
        items = items[0].split()      # get list of mail id
        print 'get {0} mail from {1}'.format(str(len(items)), author)
        return items        #split string id of matching mail


    def __init__(self, user, imap='imap.gmail.com'):
    
    # connecting to the gmail imap server
        try:
            self.m = imaplib.IMAP4_SSL(imap)
        except:
            print 'error: connection to ', imap, ' failed'
            return
        print 'connected to {0}'.format(imap)
    
    # login
        self.user = user
        self.pwd = getpass.getpass('pwd: ')
        try:
            self.m.login(self.user, self.pwd)
        except:
            print 'login {0} on {1} failed '.format(user, imap)
            return
        print 'connected as {0} on {1}'.format(user, imap)

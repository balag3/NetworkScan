import smtplib
from config import Config


class Mail():
    fromaddr = Config.load("sender")
    toaddrs  = Config.load("receiver")
    username = Config.load("mail_username")
    password = Config.load("mail_password")
    subject = "NetworkScan"


    @classmethod
    def send(cls,message,):
        msg = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (cls.fromaddr, ", ".join(cls.toaddrs), cls.subject, message)
        server = smtplib.SMTP(Config.load("server"))
        server.ehlo()
        server.starttls()
        server.login(cls.username,cls.password)
        server.sendmail(cls.fromaddr, cls.toaddrs, msg)
        server.quit()

    @staticmethod
    def format(list_to_format):
        return "The following hosts are recently connected to your network:\n" + "\n".join(i[0] + " ----- " + i[1] for i in list_to_format)

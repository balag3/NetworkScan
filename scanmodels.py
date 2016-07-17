from peewee import *
import datetime
from command import *
from connect import db
from mail import Mail




class BaseModel(Model):
    class Meta:
        database = db

class Scan(BaseModel):
    date = DateTimeField()
    network_ssid = CharField()

    @staticmethod
    def scan():
        Scan.create(date=datetime.datetime.utcnow(),network_ssid=Command.ssid())
        discovered = Command.host_discovery()
        existing = [[i.hostname,i.ip_address] for i in Host.select(Host.hostname,Host.ip_address)]
        difference = [i for i in discovered if i not in existing]
        hosts = [Host.create(hostname=i[0],ip_address=i[1]) for i in discovered]
        if difference:
            Mail.send(Mail.format(difference))

class Host(BaseModel):
    hostname = CharField()
    ip_address = CharField()
    scan = ForeignKeyField(Scan,related_name='hosts',default=Scan.select().order_by(Scan.id.desc()).limit(1))

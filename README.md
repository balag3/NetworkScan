# NetworkScan

Scans the network you are connected to and saves the hostnames,ip adresses
and the scan's timestamp into a relational postgresql database.
Sends e-mail notification if a host not recorded in the database connects to the
network.
Designed to use on a Raspberry Pi via crontab.

#### Prerequisites
* Python 3.5+
* Peewee
* Nmap
* Postgresql
* Tkinter

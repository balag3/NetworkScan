import subprocess
from subprocess import call


class Command():

    @staticmethod
    def ssid():
        ssid = subprocess.check_output(
            ['iwgetid -r'], shell=True).decode('UTF-8')
        return ssid

    @staticmethod
    def host_discovery():
        local_ip_range = ".".join(subprocess.check_output(
            ["hostname -I"], shell=True).decode('UTF-8').strip("\n").split(".")[:3] + ['0/24'])
        nmap_scan = subprocess.check_output(
            ["nmap -sP %s" % (local_ip_range)], shell=True).decode('UTF-8')
        nmap_scan = [i.split('\n') for i in nmap_scan.split(
            'Nmap scan report for ')][1:-1]
        nmap_scan = [i[0].split() for i in nmap_scan]
        result = [[i[0], i[1].strip("()")] if len(i) > 1 else [
            i[0].strip("()"), i[0].strip("()")] for i in nmap_scan]
        return result

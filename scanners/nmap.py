import nmap
import logging
import xml.etree.ElementTree as ET
import time
import subprocess
import shutil

logging.basicConfig()
log = logging.getLogger("nmap")

class Nmap:
    '''
    Wrapper for the nmap command line tool, make sure nmap is installed and in PATH. Check https://nmap.org for more info.
    '''
    def __init__(self) -> None:
        self.command = 'nmap'
        self.__check_path()
    
    def __check_path(self):
        if shutil.which(self.command) is None:
            raise FileNotFoundError(f"Could not find {self.command} in PATH")
    
    def scan(self, cidr, ports=None, args=None):
        '''
        Scan a network or host using nmap.

        cidr: CIDR notation for the network or host to scan.
        ports: Port range to scan, e.g. '1-1000'.
        args: Additional arguments to pass to nmap, separated by spaces.
        '''
        start_time = time.time()
        command = [self.command, cidr]
        if ports:
            command.append(f'-p{ports}')
        if args:
            command.extend(args.split())
        command.extend('-oX -'.split())

        result = subprocess.run(command, capture_output=True, text=True)
        result.check_returncode()
        result.stdout
        log.debug(f"{command} completed in {time.time() - start_time:.2f} seconds")
        return result.stdout
    
    def __parse_nmap_xml(xml_string):
        tree = ET.fromstring(xml_string)
        root = tree.getroot()

        for host in root.findall('host'):
            status = host.find('status').get('state')
            address = host.find('address').get('addr')
            print(f'Host {address} is {status}')
            
            if status == 'up':
                hostnames = host.find('hostnames')
                if hostnames is not None:
                    for hostname in hostnames.findall('hostname'):
                        name = hostname.get('name')
                        print(f'  Hostname: {name}')
                
                ports = host.find('ports')
                if ports is not None:
                    for port in ports.findall('port'):
                        port_id = port.get('portid')
                        protocol = port.get('protocol')
                        state = port.find('state').get('state')
                        service = port.find('service').get('name')
                        print(f'  Port {port_id}/{protocol} is {state} (Service: {service})')

a = Nmap()

p
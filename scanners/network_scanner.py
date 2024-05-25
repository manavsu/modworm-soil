import nmap
import logging
import xml.etree.ElementTree as ET
import time

logging.basicConfig()
log = logging.getLogger("ServerScanner")
log.setLevel(logging.DEBUG)

def scan_network(cidr, port='502'):
    start_time = time.time()
    nm = nmap.PortScanner()
    nm.scan(hosts=cidr, ports=port)
    open_hosts = []
    for host in nm.all_hosts():
        if nm[host].has_tcp(int(port)) and nm[host]['tcp'][int(port)]['state'] == 'open':
            open_hosts.append(host)
    log.debug(f"nmap {cidr}:{port} scanned in {time.time() - start_time:.2f} seconds")
    return open_hosts

def parse_nmap_xml(file_path):
    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Iterate over each host in the XML
    for host in root.findall('host'):
        # Get the status of the host
        status = host.find('status').get('state')
        
        # Get the IP address of the host
        address = host.find('address').get('addr')
        
        # Print the host status and address
        print(f'Host {address} is {status}')
        
        if status == 'up':
            # Get the hostnames (if any)
            hostnames = host.find('hostnames')
            if hostnames is not None:
                for hostname in hostnames.findall('hostname'):
                    name = hostname.get('name')
                    print(f'  Hostname: {name}')
            
            # Get the ports and their states
            ports = host.find('ports')
            if ports is not None:
                for port in ports.findall('port'):
                    port_id = port.get('portid')
                    protocol = port.get('protocol')
                    state = port.find('state').get('state')
                    service = port.find('service').get('name')
                    print(f'  Port {port_id}/{protocol} is {state} (Service: {service})')

# Replace 'nmap_scan.xml' with the path to your Nmap XML file
parse_nmap_xml('nmap_scan.xml')


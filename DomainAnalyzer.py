import socket
import whois
import dns.resolver
from dns.exception import DNSException
from dns.rdatatype import RdataType

def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return None

def get_dns_records(domain, record_type):
    try:
        answers = dns.resolver.resolve(domain, record_type)
        return [str(rdata) for rdata in answers]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, DNSException):
        return None

def get_whois_info(domain):
    try:
        domain_info = whois.whois(domain)
        return domain_info
    except Exception as e:
        return str(e)

def main():
    domain = input("Enter the domain name: ")

    # Get IP address
    ip_address = get_ip_address(domain)
    if ip_address:
        print(f"IP Address: {ip_address}")
    else:
        print("IP Address: Not found")

    # Get DNS records
    record_types = ['A', 'MX', 'NS', 'TXT']
    for record_type in record_types:
        records = get_dns_records(domain, record_type)
        if records:
            print(f"{record_type} Records:")
            for record in records:
                print(f"  {record}")
        else:
            print(f"{record_type} Records: Not found")

    # Get Whois information
    whois_info = get_whois_info(domain)
    if whois_info:
        print("Whois Information:")
        for key, value in whois_info.items():
            print(f"  {key}: {value}")
    else:
        print("Whois Information: Not found")

if __name__ == "__main__":
    main()

import scapy.all as scapy 
import optparse

def get_user_input():
	parse_obje = optparse.OptionParser()
	parse_obje.add_option("-i","--ipaddress",dest="ip_address",help="Enter IP Address")
	
	(user_input,arguments) = parse_obje.parse_args()
	
	if not user_input.ip_address:
		print("Enter IP Address")
		
	return user_input
		

def scan_my_network(ip):	
	arp_request_packet = scapy.ARP(pdst=ip)			
	broadcast_packet = scapy_Ether(dst="ff:ff:ff:ff:ff:ff") 	
	comnined_packet = broadcast_packet/arp_request_packet		
	(answered_list,unanswered_list) = scapy_srp(comnined_packet,timeout=1)
	
	answered_list.summary()
	
user_ip_address = get_user_input()
scan_my_network(user_ip_address.ip_address)


 
 
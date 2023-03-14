from scapy.all import *
from scapy.layers.inet import IP, UDP

# Définir l'adresse IP source et destination
src_ip = "192.168.149.130"
dst_ip = "192.168.149.130"

# Définir les numéros de port source et destination
src_port = 1234
dst_port = 80

# Créer un paquet UDP avec un message
udp_packet = IP(src=src_ip, dst=dst_ip) / UDP(sport=src_port, dport=dst_port) / "Bonjour, ceci est un paquet UDP."

# Envoyer le paquet plusieurs fois pour générer du trafic
send(udp_packet, count=1, inter=0.5)
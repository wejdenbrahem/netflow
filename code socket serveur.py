def packet_filter(data):
    # Vérifier si les données sont une requête HTTP
    if "HTTP" in data:
        print(data)

# Créer un socket et écouter sur le port 1234 en utilisant UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("127.0.0.1", 1234))

print("Server started. Listening on port 1234...")

# Recevoir les paquets et les traiter
while True:
    data, address = server_socket.recvfrom(1024)
    packet_filter(data.decode('utf-8', errors='ignore'))

# Fermer le socket
server_socket.close()
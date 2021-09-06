import socket


HOST = '0.0.0.0'
PORT = 1337
BUFFER_SIZE = 1024

ADD_PREFIX_COMMAND = 'ADD '

DOMAINS = {}


if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    address = HOST, PORT

    server_socket.bind(address)
    print(f'Server listening on {HOST}:{PORT}')
    while True:
        received_data, sender = server_socket.recvfrom(BUFFER_SIZE)
        received_data = received_data.decode().strip()

        if received_data.startswith(ADD_PREFIX_COMMAND):
            received_data = received_data.lstrip(ADD_PREFIX_COMMAND)
            if received_data.count(':') != 1:
                server_socket.sendto(b'Incorrect syntax for the update domain address command.\n', sender)
                continue

            host, ip_addr = received_data.split(':')
            DOMAINS[host] = ip_addr
            server_socket.sendto(b'Domain address has been successfully updated.\n', sender)
        elif received_data in DOMAINS:
            server_socket.sendto(DOMAINS[received_data].encode() + b'\n', sender)
        else:
            try:
                ip_addr = socket.gethostbyname(received_data)
            except socket.gaierror:
                server_socket.sendto(b'Unknown domain name\n', sender)
            else:
                server_socket.sendto(ip_addr.encode() + b'\n', sender)

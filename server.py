import socket

clients = []

def start_game():
    while True:
        
        s1, addr1=clients[0]
        s2, addr2=clients[1]
        
        mv1= s1.recv(1024)
        mv1 = mv1.decode('utf-8').strip()
        
        mv2=s2.recv(1024)
        mv2 = mv2.decode('utf-8').strip()
        
        if mv1 == mv2:
            s1.sendall(b"It's a tie")
            s2.sendall(b"It's a tie")
        elif (mv1 == 'R' and mv2 == 'S') or (mv1 == 'P' and mv2 == 'R') or (mv1 == 'S' and mv2 == 'P'):
            s1.sendall(b"You won")
            s2.sendall(b"You lost")
        else:
            s1.sendall(b"You lost")
            s2.sendall(b"You won")
            
        mv1=s1.recv(1024)
        mv1=mv1.decode('utf-8').strip()
        
        mv2=s2.recv(1024)
        mv2=mv2.decode('utf-8').strip()
        
        if (mv1.lower()=="quit"):
            s2.sendall(b"game ended")
            s1.sendall(b"game ended")
            s1.close()
            s2.close()
            return
        elif (mv2.lower()=="quit"):
            s1.sendall(b"game ended")
            s2.sendall(b"game ended")
            s1.close()
            s2.close()
            return
        elif (mv1.lower()=="yes") and (mv2.lower()=="yes"):
            s1.sendall(b"game continue")
            s2.sendall(b"game continue")
            continue
        

    #s1.close()
    #s2.close()

def start_server(host='127.0.0.1', port=65244):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    
    server_socket.listen(2)
    print(f"Server listening on {host}:{port}")
    for i in range (2):
        client_socket, client_address = server_socket.accept()
        print(f"Connected to {client_address}")
        clients.append((client_socket, client_address))

    start_game()
    
    server_socket.close()

if __name__ == "__main__":
    start_server()

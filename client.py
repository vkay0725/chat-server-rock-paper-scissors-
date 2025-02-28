import socket

def start_client(host='127.0.0.1', port=65244):
    client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect((host,port))
    print(f"connnected to server at {host}:{port}")
    
    
    while True:
        message=input("Enter move(R/P/S):")
        client_socket.sendall(message.encode('utf-8'))
        
        response=client_socket.recv(1024)
        print(f"received from server :{response.decode('utf-8')}")
        
        message=input("wish to continue?(yes/quit):")
        client_socket.sendall(message.encode('utf-8'))
        
        
        response=client_socket.recv(1024)
        response=response.decode('utf-8')
        if response == "game ended":
            client_socket.close()
            break
    
if __name__=="__main__":
    start_client()

    
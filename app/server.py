import socket

def mock_peer(port=6881):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind(("0.0.0.0", port))
        server.listen(1)
        print(f"Mock peer running on port {port}")
        conn, addr = server.accept()
        with conn:
            print(f"Connected by {addr}")
            handshake = conn.recv(68)
            print(f"Received handshake: {handshake}")
            conn.send(handshake) 
mock_peer()

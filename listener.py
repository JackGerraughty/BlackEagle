import socket
import threading

def handle_client(conn):
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data.decode())
    except Exception as e:
        print(e)
    finally:
        conn.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 4444))
server.listen(5)

while True:
    client, addr = server.accept()
    print(f"[+] Connected to {addr[0]}:{addr[1]}")
    threading.Thread(target=handle_client, args=(client,)).start()
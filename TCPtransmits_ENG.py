import socket
import subprocess
import elevate
import zipfile
import os
import time
import keyboard
from colorama import Fore, Style, init

# Khởi tạo colorama
init(autoreset=True)

SEND_FOLDER = 'sending'
ZIP_FILE = 'send_data.zip'
RECEIVE_FOLDER = 'received'
SERVER_IP = '0.0.0.0'
PORT = 5000

# Yêu cầu quyền admin
elevate.elevate()

# Hàm để xóa màn hình
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def progress_loading(message, total_steps, step_duration=1):
    bar_length = 40  
    print(Fore.GREEN + message)
    for step in range(total_steps + 1):
        percent = int((step / total_steps) * 100)
        num_hashes = int((step / total_steps) * bar_length)
        num_spaces = bar_length - num_hashes
        bar = f"[{'-' * num_hashes}{' ' * num_spaces}] {percent}%"
        print(Fore.YELLOW + bar, end="\r")
        time.sleep(step_duration)
    print(Fore.GREEN + "\nDone!\n")



# Hàm in menu trong khung và căn chỉnh cho cân xứng
def print_menu():
    clear_screen()
    print(Fore.CYAN + center_text("=" * 50))  # Căn giữa đường kẻ trên
    print(Fore.CYAN + center_text("MENU"))  # Căn giữa tiêu đề "MENU"
    print(Fore.CYAN + center_text("=" * 50))
    print(Fore.CYAN + center_text("Enter your choice:"))
    menu_box = [
        " _____________________ ",
        "| 1. Get IP address   |",
        "| 2. Open Port 5000   |",
        "| 3. Send file        |",
        "| 4. Receive file     |",
        "| 5. Quit             |",
        "|_____________________|"
    ]

    for line in menu_box:
        print(Fore.YELLOW + center_text(line))
    print(Fore.WHITE + center_text("Copyright © 2024 NhatAn."))

def center_text(text):
    columns = os.get_terminal_size().columns
    return text.center(columns)

def get_ip_address():
    clear_screen()
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    progress_loading("Get IP address", 1)
    print(Fore.GREEN + center_text(f"The computer's IP address: {ip_address}"))
    input(Fore.YELLOW + center_text("\nPress any key to return to the menu..."))

def open_port(port=5000):
    clear_screen()
    progress_loading("Open port", 5)
    try:
        command = f"netsh advfirewall firewall add rule name=\"Open Port {port}\" dir=in action=allow protocol=TCP localport={port}"
        subprocess.run(command, shell=True, check=True)
        print(Fore.GREEN + center_text('Open port successfully'))
    except subprocess.CalledProcessError as e:
        print(Fore.RED + center_text(f'Cannot open port {port}. Error: {e}'))
    input(Fore.YELLOW + center_text("\nPress any key to return to the menu..."))

def unzip_file(zip_file, extract_to):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(Fore.GREEN + center_text(f"The file has been unzipped at: {extract_to}"))

def delete_zip_file(zip_file):
    if os.path.exists(zip_file):
        os.remove(zip_file)
        print(Fore.GREEN + center_text(f"Deleted zip file: {zip_file}"))
    else:
        print(Fore.RED + center_text(f"The zip file does not exist: {zip_file}"))

def receive_file():
    clear_screen()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((SERVER_IP, PORT))
        server_socket.listen()
        print(Fore.GREEN + center_text(f'Server is waiting for connection at {SERVER_IP}:{PORT}...'))
        conn, addr = server_socket.accept()
        with conn:
            print(Fore.GREEN + center_text(f'Connected to {addr}'))
            progress_loading("Receiving files", 5) 
            with open('received_data.zip', 'wb') as f:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    f.write(data)
            print("The zip file has been received")
            progress_loading("Unzipping the file", 5) 
            unzip_file('received_data.zip', RECEIVE_FOLDER)
            delete_zip_file('received_data.zip')
    input(Fore.YELLOW + center_text("\nPress any key to return to the menu..."))

def zip_files(folder_path, zip_name):
    clear_screen()
    print(Fore.GREEN + center_text(f"Compressing the folder {folder_path} to files {zip_name}..."))
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                zipf.write(os.path.join(root, file), file)
    progress_loading("Compressing files", 5)
    print(Fore.GREEN + center_text(f"Compress file successfully: {zip_name}"))

def send_file(zip_file, SERVER_IP, PORT):
    clear_screen()
    print(Fore.GREEN + center_text(f"Connecting to the server {SERVER_IP}:{PORT}..."))
    time.sleep(1) 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            client_socket.connect((SERVER_IP, PORT))
            print(f"Successfully connected to the server {SERVER_IP}:{PORT}")
            progress_loading("Sending files", 5) 
            with open(zip_file, 'rb') as f:
                chunk = f.read(1024)
                while chunk:
                    client_socket.sendall(chunk)
                    chunk = f.read(1024)
            print("The file has been sent successfully.")
        except Exception as e:
            print(f"Unable to connect or send files: {e}")
        finally:
            delete_zip_file(zip_file)
    input(Fore.YELLOW + center_text("\nPress any key to return to the menu..."))

def ensure_directories():
    if not os.path.exists(SEND_FOLDER):
        os.makedirs(SEND_FOLDER)
        print(Fore.GREEN + center_text(f"Folder '{SEND_FOLDER}' has been created."))
    if not os.path.exists(RECEIVE_FOLDER):
        os.makedirs(RECEIVE_FOLDER)
        print(Fore.GREEN + center_text(f"Folder '{RECEIVE_FOLDER}' has been created."))

def menu():
    ensure_directories()
    print_menu()

    while True:
        if keyboard.is_pressed('1'):
            get_ip_address()
            print_menu() 
        elif keyboard.is_pressed('2'):
            open_port(5000)
            print_menu()
        elif keyboard.is_pressed('3'):
            zip_files(SEND_FOLDER, ZIP_FILE)
            SERVER_IP = input(Fore.YELLOW + center_text("Enter the server's IP:"))
            PORT = int(input(Fore.YELLOW + center_text("Enter the server port: ")))
            send_file(ZIP_FILE, SERVER_IP, PORT)
            print_menu() 
        elif keyboard.is_pressed('4'):
            receive_file()
            print_menu()
        elif keyboard.is_pressed('5'):
            clear_screen()
            print(Fore.GREEN + center_text("QUIT."))
            break

if __name__ == "__main__":
    menu()

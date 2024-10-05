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
    """Tạo thanh loading với dạng `---------- 10%`"""
    bar_length = 40  # Độ dài của thanh loading
    print(Fore.GREEN + message)
    for step in range(total_steps + 1):
        # Tính toán tỷ lệ phần trăm
        percent = int((step / total_steps) * 100)
        # Số lượng dấu "-" và khoảng trống cần hiển thị
        num_hashes = int((step / total_steps) * bar_length)
        num_spaces = bar_length - num_hashes
        # Thanh loading động
        bar = f"[{'-' * num_hashes}{' ' * num_spaces}] {percent}%"
        print(Fore.YELLOW + bar, end="\r")
        time.sleep(step_duration)
    print(Fore.GREEN + "\nXong!\n")



# Hàm in menu trong khung và căn chỉnh cho cân xứng
def print_menu():
    clear_screen()
    print(Fore.CYAN + center_text("=" * 50))  # Căn giữa đường kẻ trên
    print(Fore.CYAN + center_text("MENU"))  # Căn giữa tiêu đề "MENU"
    print(Fore.CYAN + center_text("=" * 50))
    
    menu_box = [
        " _____________________ ",
        "| 1. Xem địa chỉ IP   |",
        "| 2. Mở cổng 5000     |",
        "| 3. Gửi file         |",
        "| 4. Nhận file        |",
        "| 5. Thoát            |",
        "|_____________________|"
    ]

    for line in menu_box:
        print(Fore.YELLOW + center_text(line))

# Hàm căn giữa text
def center_text(text):
    columns = os.get_terminal_size().columns
    return text.center(columns)

# Hàm lấy địa chỉ IP của máy tính
def get_ip_address():
    clear_screen()
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    progress_loading("Lấy địa chỉ IP", 1)
    print(Fore.GREEN + center_text(f"Địa chỉ IP của máy tính: {ip_address}"))
    input(Fore.YELLOW + center_text("\nNhấn phím bất kỳ để quay lại menu..."))

# Hàm mở cổng 5000
def open_port(port=5000):
    clear_screen()
    progress_loading("Mở port", 5)
    try:
        command = f"netsh advfirewall firewall add rule name=\"Open Port {port}\" dir=in action=allow protocol=TCP localport={port}"
        subprocess.run(command, shell=True, check=True)
        print(Fore.GREEN + center_text('Mở port thành công'))
    except subprocess.CalledProcessError as e:
        print(Fore.RED + center_text(f'Không thể mở cổng {port}. Lỗi: {e}'))
    input(Fore.YELLOW + center_text("\nNhấn phím bất kỳ để quay lại menu..."))

# Hàm giải nén file zip
def unzip_file(zip_file, extract_to):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(Fore.GREEN + center_text(f"File đã được giải nén tại: {extract_to}"))

# Hàm xóa file zip sau khi đã xử lý
def delete_zip_file(zip_file):
    if os.path.exists(zip_file):
        os.remove(zip_file)
        print(Fore.GREEN + center_text(f"Đã xóa file zip: {zip_file}"))
    else:
        print(Fore.RED + center_text(f"File zip không tồn tại: {zip_file}"))

# Hàm nhận file
def receive_file():
    clear_screen()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((SERVER_IP, PORT))
        server_socket.listen()
        print(Fore.GREEN + center_text(f'Server đang lắng nghe trên {SERVER_IP}:{PORT}...'))
        conn, addr = server_socket.accept()
        with conn:
            print(Fore.GREEN + center_text(f'Đã kết nối với {addr}'))
            progress_loading("Đang nhận file", 5)  # Loading khi nhận file
            with open('received_data.zip', 'wb') as f:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    f.write(data)
            print("File zip đã được nhận.")
            progress_loading("Đang giải nén file", 5)  # Loading khi giải nén
            unzip_file('received_data.zip', RECEIVE_FOLDER)
            delete_zip_file('received_data.zip')
    input(Fore.YELLOW + center_text("\nNhấn phím bất kỳ để quay lại menu..."))

# Hàm nén file thành file zip
def zip_files(folder_path, zip_name):
    clear_screen()
    print(Fore.GREEN + center_text(f"Đang nén thư mục {folder_path} thành file {zip_name}..."))
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                zipf.write(os.path.join(root, file), file)
    progress_loading("Đang nén file", 5)
    print(Fore.GREEN + center_text(f"Nén file thành công: {zip_name}"))

# Hàm gửi file zip qua TCP
def send_file(zip_file, SERVER_IP, PORT):
    clear_screen()
    print(Fore.GREEN + center_text(f"Đang kết nối tới server {SERVER_IP}:{PORT}..."))
    time.sleep(1)  # Thêm độ trễ mô phỏng kết nối
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            client_socket.connect((SERVER_IP, PORT))
            print(f"Đã kết nối thành công với server {SERVER_IP}:{PORT}")
            progress_loading("Đang gửi file", 5)  # Loading trong quá trình gửi file
            with open(zip_file, 'rb') as f:
                chunk = f.read(1024)
                while chunk:
                    client_socket.sendall(chunk)
                    chunk = f.read(1024)
            print("File đã được gửi thành công.")
        except Exception as e:
            print(f"Không thể kết nối hoặc gửi file: {e}")
        finally:
            delete_zip_file(zip_file)
    input(Fore.YELLOW + center_text("\nNhấn phím bất kỳ để quay lại menu..."))

# Hàm kiểm tra và tạo thư mục nếu cần
def ensure_directories():
    clear_screen()
    print(Fore.GREEN + center_text(f"Kiểm tra thư mục {SEND_FOLDER}"))
    if not os.path.exists(SEND_FOLDER):
        print(Fore.GREEN + center_text(f"Thư mục {SEND_FOLDER} không tồn tại"))
        print(Fore.GREEN + center_text(f"Tạo Thư mục {SEND_FOLDER}"))
        progress_loading("Đang tạo thư mục",5)
        os.makedirs(SEND_FOLDER)
        print(Fore.GREEN + center_text(f"Thư mục '{SEND_FOLDER}' đã được tạo."))
    else:
        print(Fore.GREEN + center_text(f"Thư mục '{SEND_FOLDER}' đã tồn tại"))
    print(Fore.GREEN + center_text(f"Kiểm tra thư mục {RECEIVE_FOLDER}"))  
    if not os.path.exists(RECEIVE_FOLDER):
        print(Fore.GREEN + center_text(f"Thư mục {RECEIVE_FOLDER} không tồn tại"))
        print(Fore.GREEN + center_text(f"Tạo Thư mục {RECEIVE_FOLDER}"))
        progress_loading("Đang tạo thư mục",5)
        os.makedirs(RECEIVE_FOLDER)
        print(Fore.GREEN + center_text(f"Thư mục '{RECEIVE_FOLDER}' đã được tạo."))
    else:
        print(Fore.GREEN + center_text(f"Thư mục '{RECEIVE_FOLDER}' đã tồn tại"))

# Menu giao diện dòng lệnh
def menu():
    ensure_directories()
    print_menu()

    while True:
        # Đọc phím nhấn mà không cần nhấn Enter
        if keyboard.is_pressed('1'):
            get_ip_address()
            print_menu()  # Quay lại menu sau khi xem IP
        elif keyboard.is_pressed('2'):
            open_port(5000)
            print_menu()  # Quay lại menu sau khi mở cổng
        elif keyboard.is_pressed('3'):
            zip_files(SEND_FOLDER, ZIP_FILE)
            SERVER_IP = input(Fore.YELLOW + center_text("Nhập IP của server: "))
            PORT = int(input(Fore.YELLOW + center_text("Nhập cổng của server: ")))
            send_file(ZIP_FILE, SERVER_IP, PORT)
            print_menu()  # Quay lại menu sau khi gửi file
        elif keyboard.is_pressed('4'):
            receive_file()
            print_menu()  # Quay lại menu sau khi nhận file
        elif keyboard.is_pressed('5'):
            clear_screen()
            print(Fore.GREEN + center_text("Thoát chương trình."))
            break

if __name__ == "__main__":
    menu()

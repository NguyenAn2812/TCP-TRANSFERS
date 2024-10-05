
# TCP Transfers

**TCP Transfers** is a file transfer application that utilizes the TCP protocol for reliable data transmission. 
This application allows users to send and receive files securely over the network with a user-friendly interface.

TCP Transfers là một ứng dụng chuyển tập tin sử dụng giao thức TCP để truyền dữ liệu một cách đáng tin cậy.
Ứng dụng này cho phép người dùng gửi và nhận các tệp một cách an toàn qua mạng với giao diện thân thiện với người dùng.

---

## Key Features

- **View IP Address**: Displays the IP address of the machine to identify the network.
- **Open Port 5000**: Opens a specific port to allow TCP connections.
- **File Transfer**: Send and receive files between devices using the TCP protocol.
- **Compression & Decompression**: Automatically compress files before sending and decompress after receiving.
- **Progress Bar**: Shows a progress bar during the file transfer process, providing visual feedback to users.

Các Tính Năng Chính:

- **Xem Địa Chỉ IP**: Hiển thị địa chỉ IP của máy để xác định mạng.
- **Mở Cổng 5000**: Mở một cổng cụ thể để cho phép kết nối TCP.
- **Chuyển Tệp**: Gửi và nhận tệp giữa các thiết bị sử dụng giao thức TCP.
- **Nén & Giải Nén**: Tự động nén các tệp trước khi gửi và giải nén sau khi nhận.
- **Thanh Tiến Trình**: Hiển thị thanh tiến trình trong quá trình chuyển tệp, cung cấp phản hồi trực quan cho người dùng.

---

## Installation Guide

1. **Download the Installer**: You can download the installer for both languages below:
   - [Download English Version (tcptrans_ENG.exe)](https://github.com/NguyenAn2812/TCP-TRANSFERS/releases/download/v1.0.0/TCPtransmits_ENG.exe)
   - [Download Vietnamese Version (tcptrans_VN.exe)](https://github.com/NguyenAn2812/TCP-TRANSFERS/releases/download/v1.0.0/TCPtransmits_VN.exe)

2. **Place the `tcptrans.exe` file in a separate folder**. This ensures that all generated folders and files stay organized within this folder.

Hướng Dẫn Cài Đặt:

1. **Tải xuống Trình cài đặt**: Bạn có thể tải xuống trình cài đặt cho cả hai ngôn ngữ dưới đây:
   - [Tải phiên bản tiếng Anh (tcptrans_ENG.exe)](https://github.com/NguyenAn2812/TCP-TRANSFERS/releases/download/v1.0.0/TCPtransmits_ENG.exe)
   - [Tải phiên bản tiếng Việt (tcptrans_VN.exe)](https://github.com/NguyenAn2812/TCP-TRANSFERS/releases/download/v1.0.0/TCPtransmits_VN.exe)

2. **Đặt file `tcptrans.exe` vào một thư mục riêng**. Điều này đảm bảo rằng tất cả các thư mục và tệp được tạo ra sẽ được sắp xếp gọn gàng trong thư mục này.

---

## Detailed Usage Instructions

### First Time Running the Application

- After installation, you need to **place the `tcptrans.exe` file** in a **separate folder**.
- When you **run the software for the first time**, it will automatically **create two folders**:
  - **`Sending`**: This folder will store the files you want to send.
  - **`Receive`**: This folder will store the files you receive.
- Once the application starts, you will see the following menu options:

```bash
============================
            MENU
============================
 ________________________
| 1. View IP Address        |
| 2. Open Port 5000         |
| 3. Send File              |
| 4. Receive File           |
| 5. Exit                   |
|___________________________|
```

Hướng Dẫn Sử Dụng Chi Tiết:

### Lần Đầu Chạy Ứng Dụng

- Sau khi cài đặt, bạn cần **đặt file `tcptrans.exe` vào một thư mục riêng**.
- Khi bạn **chạy phần mềm lần đầu tiên**, nó sẽ tự động **tạo hai thư mục**:
  - **`Sending`**: Thư mục này sẽ lưu trữ các tệp bạn muốn gửi.
  - **`Receive`**: Thư mục này sẽ lưu trữ các tệp bạn nhận.
- Khi ứng dụng khởi động, bạn sẽ thấy các tùy chọn menu sau:

```bash
============================
            MENU
============================
 ________________________
| 1. Xem Địa Chỉ IP         |
| 2. Mở Cổng 5000           |
| 3. Gửi Tệp                |
| 4. Nhận Tệp               |
| 5. Thoát                  |
|___________________________|
```

---

## Troubleshooting

If you encounter issues while using the application, try the following:

- **IP Address Issues**: Ensure the IP address is correct and the devices are on the same network.
- **Port Not Open**: Make sure port 5000 is open on the receiver's device. You can open it using **Option 2** from the menu.
- **File Not Sent**: Make sure the file exists in the **Sending** folder, and ensure the recipient is ready to receive the file.

Khắc Phục Sự Cố:

Nếu gặp sự cố khi sử dụng ứng dụng, hãy thử những điều sau:

- **Sự Cố Địa Chỉ IP**: Đảm bảo địa chỉ IP là chính xác và các thiết bị đang nằm trong cùng một mạng.
- **Cổng Không Mở**: Đảm bảo rằng cổng 5000 đã được mở trên thiết bị nhận. Bạn có thể mở nó bằng cách chọn **Tùy chọn 2** trong menu.
- **Tệp Không Được Gửi**: Đảm bảo rằng tệp tồn tại trong thư mục **Sending**, và người nhận đã sẵn sàng nhận tệp.

---

## Acknowledgment

This application was conceived as a personal project to solve the need for easy file transfer between devices. I developed this utility out of curiosity and necessity, and I want to clarify that I did not intend to copy anyone's ideas or concepts. This project is not intended for commercial use and is shared solely for educational and personal purposes.

Lời Cảm Ơn:

Ứng dụng này được sáng tạo như một dự án cá nhân để giải quyết nhu cầu truyền tệp dễ dàng giữa các thiết bị. Tôi phát triển tiện ích này vì tò mò và do nhu cầu, và tôi muốn làm rõ rằng tôi không có ý định sao chép ý tưởng hay khái niệm của bất kỳ ai. Dự án này không nhằm mục đích thương mại và chỉ được chia sẻ cho mục đích giáo dục và cá nhân.


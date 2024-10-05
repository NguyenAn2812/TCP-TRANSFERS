# TCP Transfers

**TCP Transfers** is a file transfer application that utilizes the TCP protocol for reliable data transmission. This application allows users to send and receive files securely over the network with a user-friendly interface.

---

## Key Features

- **View IP Address**: Displays the IP address of the machine to identify the network.
- **Open Port 5000**: Opens a specific port to allow TCP connections.
- **File Transfer**: Send and receive files between devices using the TCP protocol.
- **Compression & Decompression**: Automatically compress files before sending and decompress after receiving.
- **Progress Bar**: Shows a progress bar during the file transfer process, providing visual feedback to users.

---

## Installation Guide

1. **Download the Installer**: You can download the installer for both languages below:
   - [Download English Version (tcptrans_ENG.exe)](#)
   - [Download Vietnamese Version (tcptrans_VN.exe)](#)

2. **Place the `tcptrans.exe` file in a separate folder**. This ensures that all generated folders and files stay organized within this folder.


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
## Detailed Usage Instructions

### 1. View IP Address
- Select **Option 1** to display your device's IP address.
  
  **Important Note**: When sending files, you must know the IP address of the recipient's machine. The recipient can view their IP address using **Option 1** on their side.

### 2. Open Port 5000
- Select **Option 2** to open port 5000, allowing TCP connections to the device.

  **Important Note**: If you are receiving files, ensure that port 5000 is open. If you're not sure whether the port is open, choose **Option 2** to open it.

### 3. Send File
- Select **Option 3** to send a file.

  **Important Note**: You need to know the IP address of the recipient's machine. The recipient can check their IP address using **Option 1** on their side. After selecting a file from your **Sending** folder, the software will automatically compress it before sending.

### 4. Receive File
- Select **Option 4** to receive a file.

  **Important Note**: Make sure port 5000 is open on your machine. If it's not open or you're unsure, select **Option 2** to open it. The file will be saved to the **Receive** folder and decompressed automatically.

---

## Technical Stack
- **Programming Language**: Java (for TCP connections and file handling).
- **Standalone Executable**: The application is a self-contained executable; no additional installations or configurations are needed.

---

## Troubleshooting
If you encounter issues while using the application, try the following:

- **IP Address Issues**: Ensure the IP address is correct and the devices are on the same network.
- **Port Not Open**: Make sure port 5000 is open on the receiver's device. You can open it using **Option 2** from the menu.
- **File Not Sent**: Make sure the file exists in the **Sending** folder, and ensure the recipient is ready to receive the file.

For further assistance, feel free to contact us at [support@nhatan.com](mailto:nguyentrannhatan2812@gmail.com).


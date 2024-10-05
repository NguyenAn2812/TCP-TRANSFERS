# File Transfer Utility

## Overview

The File Transfer Utility is a Python-based application designed for seamless file sending and receiving over a network. This tool allows users to easily share files by creating zip archives, managing firewall settings, and handling file transfers efficiently.

## Features

- **View Local IP Address**: Quickly display the local IP address of your machine.
- **Open Firewall Port**: Automatically open TCP port 5000 to allow incoming connections for file transfers.
- **Send Files**: Compress and send files from a specified directory to a remote server.
- **Receive Files**: Receive incoming files and automatically extract them to a designated folder.
- **User-Friendly Menu**: Simple and interactive command-line interface for easy navigation.

## Requirements

- Python 3.x
- Required Python packages:
  - `socket`
  - `subprocess`
  - `elevate`
  - `zipfile`
  - `os`

## Installation

# Net Scanner

A multithreaded TCP port scanner written in Python for network scanning and educational purposes.

---

## Overview

This tool scans TCP ports on one or multiple targets and reports open ports.  
It is designed for learning networking concepts, concurrency, and building CLI tools in Python.

---

## Features

- TCP port scanning
- Multithreading for faster scans
- Multiple target support
- Configurable port ranges
- Fast scan mode
- Simple CLI interface

---


## Requirements

- Python 3.8+

No external dependencies required (standard library only).

---

## Usage

### Basic scan
```bash
python main.py 127.0.0.1 --ports 1-1000
```

### Deep scan
```bash
python main.py 8.8.8.8 --mode deep
```

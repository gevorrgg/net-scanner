import socket

def connect(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.2)

        s.connect((str(target), port))
        s.close()

        return True
    except:
        return False
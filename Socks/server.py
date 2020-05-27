import socket

s = socket.socket()
print('Socket Created')

s.bind(('localhost', 9999))

s.listen(3)
print('waiting for connections')

while True:
    c, addr = s.accept()
    print('connected with ', addr)
    name = c.recv(1024).decode()
    
    c.send(bytes('Welcome to OFI', 'utf-8'))

    c.close()
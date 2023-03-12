import socketserver


class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip().decode('utf-8')
        if self.data[0] == 'A' or self.data[0] == 'a':
            s = ''.join(sorted(self.data[1:]))
        elif self.data[0] == 'D' or self.data[0] == 'd':
            s = ''.join(sorted(self.data[1:]))[::-1]
        elif self.data[0] == 'C' or self.data[0] == 'c':
            s = self.data[1:].upper()
        else:
            s = self.data
        # print(s)
        self.request.sendall(bytes(s, 'utf-8'))
    

if __name__=='__main__':
    HOST, PORT = 'localhost', 9999


    with socketserver.TCPServer((HOST,PORT), TCPHandler) as server:
        server.serve_forever()
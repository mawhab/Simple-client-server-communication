import socketserver


class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip().decode('utf-8')
        if self.data[0] == 'A':
            s = ''.join(sorted(self.data[1:]))
        elif self.data[0] == 'D':
            s = ''.join(sorted(self.data[1:]))[::-1]
        elif self.data[0] == 'C':
            s = self.data[1:].upper()
        else:
            s = self.data
        print(s)
        self.request.sendall(bytes(s, 'utf-8'))
    

if __name__=='__main__':
    HOST, PORT = 'localhost', 9999


    with socketserver.TCPServer((HOST,PORT), TCPHandler) as server:
        server.serve_forever()
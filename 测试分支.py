from socket import *
from select import *


class UdpChatServer():
    def __init__(self, ADDR):
        self.addr = ADDR
        self.U = socket(AF_INET, SOCK_DGRAM)
        self.U.bind(ADDR)
        self.user = {}

    def links(self, name, addr):
        if name not in self.user:
            self.U.sendto("OK".encode(), addr)
            self.user[name] = addr
            for k in self.user:
                if k != name:
                    sk = "/n欢迎%s进入聊天室" % name
                    self.U.sendto(sk.encode(), self.user[k])
        else:
            self.U.sendto("NO".encode(), addr)

    def put_message(self, name, message, addr):
        sl = "/n %s :>> %s" % (name, message)
        for k in self.user:
            if self.user[k] != addr:
                self.U.sendto(sl.encode(), self.user[k])

    def start(self):
        while True:
            data, addr = self.U.recvfrom(2048)
            l = data.decode().split(" ", 2)
            print(l)
            if l[0] == "L":
                self.links(l[1], addr)
            if l[0] == "P":
                self.put_message(l[1], l[2], addr)


def main():
    ADDR = ("0.0.0.0", 9999)
    UDP = UdpChatServer(ADDR)
    UDP.start()


if __name__ == "__main__":
    main()

from socket import *
from select import *
from multiprocessing import Process


class UdpCharCilent():
    def __init__(self, ADDR):
        self.ADDR = ADDR
        self.U = socket(AF_INET, SOCK_DGRAM)

    def enter(self):
        while True:
            name = input("请输入您的用户名：")
            self.U.sendto(("L " + name).encode(), self.ADDR)
            data, addr = self.U.recvfrom(1024)
            print(data.decode())
            if data.decode() != "OK":
                print("您输入的用户名存在,请重新输入")
            else:
                return name

    def get(self):
        while True:
            data, addr = self.U.recvfrom(1024)
            print(data.decode())

    def put(self, name):
        while True:
            mesg = input("<<")
            self.U.sendto(("P " + " " + name + mesg).encode(), self.ADDR)

    def start(self):
        name = self.enter()

        p = Process(target=self.get)
        p.daemon = True
        p.start()

        self.put(name)


def main():
    ADDR = ("127.0.0.1", 9999)
    UDP = UdpCharCilent(ADDR)
    UDP.start()


if __name__ == "__main__":
    main()

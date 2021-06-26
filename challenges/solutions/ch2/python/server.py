#!/usr/bin/env python3

import socket

addr = ("", 1337)


def main():
    global addr
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(addr)
        s.listen()
        conn, addr = s.accept()
        with conn:
            while True:
                


if __name__ == "__main__":
    main()

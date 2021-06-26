#!/usr/bin/env python3
'''
---------------------------- SERVER.PY ----------------------------
This server was created as part of the 100 Red Team Projects
solutions. This is most definitely NOT a production-grade server -
please don't try to use it as such.

- sp1icer
-------------------------------------------------------------------
'''

import selectors
import socket
import types

# Setting the server listening address.
server_addr = ("", 1337)
sel = selectors.DefaultSelector()


def accept_wrapper(sock):
    conn, client_addr = sock.accept()
    print('[+] Connection from: ' + str(client_addr))
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=client_addr, inb=b'', outb=b'')
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)


def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)
        if recv_data:
            data.outb += recv_data
        else:
            print('[-] Closing connection to: ' + str(data.addr))
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print('[+] Echoing: ' + str(data.outb))
            sent = sock.send(data.outb)
            data.outb = data.outb[sent:]


def server_init():
    global server_addr
    print("[*] Initializing server")
    with socket.socket( socket.AF_INET, socket.SOCK_STREAM ) as sock:
        sock.bind(server_addr)
        sock.listen()
        sock.setblocking(False)
        sel.register(sock, selectors.EVENT_READ, data=None)
        while True:
            events = sel.select(timeout=None)
            for key, mask in events:
                if key.data is None:
                    accept_wrapper(key.fileobj)
                else:
                    service_connection(key, mask)


def main():
    server_init()


if __name__ == "__main__":
    main()

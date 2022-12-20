import contextlib
import socket
import subprocess
import filemod
import threading
def listern():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('192.168.1.100',8080))

    print("[server] started and listening...")

    s.listen(2)
    filemod.writer("temp.py","","w")
    client,addr = s.accept()
    print(f"[server] connected to {addr}")
    t1=threading.Thread(target=handel,args=(client,s))
    t1.start()


def handel(client,s):
    cmdlet = client.recv(2048).decode()

    while cmdlet != 'quit':
        filemod.writer("temp.py","from boxdb import *"+"\n"+cmdlet,"w")
        cmdlet=str(cmdlet)
        try:
            result = subprocess.check_output("python temp.py",shell=True)
            if result == bytes("", 'utf-8'):
                result=bytes("none", 'utf-8')
            client.send(result)
            cmdlet = client.recv(2048).decode()
        except Exception as e:
            print(e)
            with contextlib.suppress(Exception):
                client.send(bytes("couldnot", 'utf-8'))
            s.close()
            listern()
    listern()


listern()
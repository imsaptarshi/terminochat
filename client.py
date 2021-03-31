import socket
import threading

nickname=input("Choose a nickname: ")

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("172.18.0.1",40280))

def receive():
    while True:
        try:
            msg=client.recv(1024).decode("ascii")
            if msg=="NICK":
                client.send(nickname.encode("ascii"))
            else:
                print(msg)
        except:
            print("Brr an error occured...")
            client.close()
            break

def write():
    while True:
        msg=f"\033[92m{nickname}\033[00m: {input('')}"
        client.send(msg.encode("ascii"))

receive_thread=threading.Thread(target=receive)
receive_thread.start()

write_thread=threading.Thread(target=write)
write_thread.start()

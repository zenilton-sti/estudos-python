import socket
import json 

js={}
js["nome"]="zenilton"

print(js)

ip_local = socket.gethostbyname(socket.gethostname())
print(f'IP Local: {ip_local}')
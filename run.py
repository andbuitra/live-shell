import paramiko

# Vars declaration
guest_addr = "192.168.0.104"
user = "root"
passwd = "Asd123asd123!"

client = paramiko.SSHClient()
client.load_system_host_keys()

conn = client.connect(hostname=guest_addr, username=user, password=passwd)


while True:
    cmd = input("Ejecutar comando: ")
    if cmd == "exit":
        print("Conexión cerrada")
        client.close()
        exit()
    stdin, stdout, stderr = client.exec_command(cmd)
    print(stdout.read().decode(encoding='UTF-8'))

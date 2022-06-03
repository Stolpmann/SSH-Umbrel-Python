import paramiko
import secrets
import pandas as pd

host = secrets.host
port = secrets.port
username = secrets.username
password = secrets.password

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)


networkhashps = []

def scraper():
    x = 1
    while x < 25:
        command = f"docker exec bitcoin bitcoin-cli getnetworkhashps -1 {x}"
        stdin, stdout, stderr = ssh.exec_command(command)
        hashps = stdout.readlines()
        print(hashps)
        networkhashps.append([hashps[0]])
        x += 1
scraper()

df = pd.DataFrame(networkhashps)


df.to_csv('mining/networkhashps.csv', index=False)

print(networkhashps)

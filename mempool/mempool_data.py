import paramiko
import secrets
import pandas as pd

host = secrets.host
port = secrets.port
username = secrets.username
password = secrets.password

command = "docker exec bitcoin bitcoin-cli getrawmempool true"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

stdin, stdout, stderr = ssh.exec_command(command)
lines = stdout.readlines()

print(lines)

df = pd.DataFrame(lines, columns=['name', 'swag'])
df.to_csv("mempool/mem_data.csv")
print(df)

vsize = []
weight = []
fee = []
modifiedfee = []
time = []
height = []
descendantcount = []
descendantsize = []
descendantfees = []
ancestorcount = []
ancestorsize = []
ancestorfees = []
depends = []

def scraper():
    lst = []
    for x in lines:
        y = 0
        while y < 22:
            lst.append(lines[1])
            y += 1

scraper()

del stdin
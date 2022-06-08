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


del stdin
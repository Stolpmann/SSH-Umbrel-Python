import paramiko
import secrets
#import pandas as pd

host = secrets.host
port = secrets.port
username = secrets.username
password = secrets.password

command = "docker exec bitcoin bitcoin-cli getblockcount"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

stdin, stdout, stderr = ssh.exec_command(command)
blockheight = stdout.readlines()


blockheight = int(blockheight[0])

print(blockheight)


stats = """'["totalfee","avgfeerate", "avgfee"]'"""

x = 700000


lst = []

while x < 700100:
    command2 = f"docker exec bitcoin bitcoin-cli getblockstats {x} {stats}"
    stdin, stdout, stderr = ssh.exec_command(command2)
    blockstats = stdout.readlines()
    lst.append([blockstats[1:4]])
    print(blockstats)
    x += 1

print(lst)
print(len(lst))

# command2 = f"docker exec bitcoin bitcoin-cli getblockstats {blockheight} {stats}"
# stdin, stdout, stderr = ssh.exec_command(command2)
# blockstats = stdout.readlines()
#
# print(blockstats)

del stdin
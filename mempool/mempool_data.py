import paramiko
import secrets
import pandas as pd
import numpy as np

host = secrets.host
port = secrets.port
username = secrets.username
password = secrets.password



command = f"docker exec bitcoin bitcoin-cli getrawmempool true"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

stdin, stdout, stderr = ssh.exec_command(command)
lines = stdout.readlines()


df = pd.DataFrame(lines)


df.to_csv('mempool/memdata.csv')

# print(len(lines))
#
# # length = lines[:27]
# #
# # length2 = lines[27:54]
#
# def mem_scraper():
#     mempool = []
#     for z in lines:
#         if len(lines) < 27:
#             return mempool
#         length = lines[:27]
#         mempool.append(length)
#         del lines[:27]
#     return mempool
#
#
#
# data = mem_scraper()
#
# df = pd.DataFrame(data)
#
#
# df.to_csv('mempool/memdata.csv')

del stdin
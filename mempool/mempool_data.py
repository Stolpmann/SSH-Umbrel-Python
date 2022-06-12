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

print(len(lines))

def fee_scraper():
    fees = '"fee"'
    lst = []
    for x in lines:
        if fees in x:
            lst.append(x)
    return lst

fees = fee_scraper()

print(type(fees))


def vsize_scraper():
    vsize = '"vsize"'
    lst = []
    for x in lines:
        if vsize in x:
            lst.append(x)
    return lst

vsize = vsize_scraper()

print(type(vsize))

df = list(zip(fees,vsize))

df2 = pd.DataFrame(df, columns=['fees','vsize'])

df2.to_csv('mempool/memdata.csv')

# df.to_csv('mempool/memdata.csv')

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
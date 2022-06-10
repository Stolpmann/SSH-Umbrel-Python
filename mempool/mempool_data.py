import paramiko
import secrets
import pandas as pd
import numpy as np

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

df = pd.DataFrame(lines)

df.to_csv('mempool/memdata.csv')
length = len(lines)
print(np.array_split(df, ))



# transactionid = []
# vsize = []
# weight = []
# fee = []
# modifiedfee = []
# time = []
# height = []
# descendantcount = []
# descendantsize = []
# descendantfees = []
# ancestorcount = []
# ancestorsize = []
# ancestorfees = []
# wtxid = []
# fees = []
# base = []
# modified = []
# ancestor = []
# descendant = []
# depends = []
# spentby = []
# bip125_replaceable = []
# unbroadcast = []



del stdin
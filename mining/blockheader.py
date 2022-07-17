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

# reads clean block data
df = pd.read_csv("block_stats/clean_block_data.csv")


# Iterates using blockhash to call block header rpc command
hashes = df['blockhash'].tolist()
lst = []

def getblockheader():
    for hash in hashes:
        command = f"docker exec bitcoin_bitcoind_1 bitcoin-cli getblockheader {hash}"
        stdin, stdout, stderr = ssh.exec_command(command)
        lines = stdout.readlines()
        lst.append(lines)
        del stdin
    return lst

getblockheader()
print(lst)

df2 = pd.DataFrame(lst)

df2.to_csv("mining/blockheader_data.csv")
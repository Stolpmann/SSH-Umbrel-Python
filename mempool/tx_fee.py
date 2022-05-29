import paramiko
import secrets


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
print(type(lines))

# Get user input of transaction
txid = input("Enter TXID: ")

print(txid)

# Parses through mempool returning index of txid in mempool list
def mempool_parser(txid):
    y = 0
    for x in lines:
        if txid in x:
            return y
        y += 1


y = mempool_parser(txid)
print(mempool_parser(txid))


# Slice tx data from mempool list
tx_data = lines[y:y+27]
print(tx_data)

# Extract vsize
vsize = tx_data[7]
vsize = vsize[13:-2]
vsize = int(vsize)

# Extract fee
fee = tx_data[9]
fee = fee[11:-2]
fee = float(fee)
fee = fee * 100000000

# Fee rate (sats/vbyte)
sats_per_vbyte = fee/vsize


# Print Results
print(vsize)
print(format(fee,'.00000000f'))
print(format(sats_per_vbyte, 'f'))

# vsize



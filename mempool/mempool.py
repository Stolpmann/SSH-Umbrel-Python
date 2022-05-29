import paramiko
import secrets

host = secrets.host
port = secrets.port
username = secrets.username
password = secrets.password

command = "docker exec bitcoin bitcoin-cli getrawmempool"


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)


stdin, stdout, stderr = ssh.exec_command(command)
lines = stdout.readlines()
print("\n")

# prompts user for TXID and then loops through to check mempool

def find_transaction(txid):
    transaction = [i for i in lines if txid in i]
    if len(transaction) != 0:
        return transaction[0]
    else:
        print("TXID is not in current Mempool")

txid = input("Enter TXID: ")

while len(txid) < 64:
    print("TXID must be 64 characters")
    txid = input("Enter TXID: ")

x = find_transaction(txid)
x = str(x)
x = x[1:-2]
print("\n")

command2 = f"docker exec bitcoin bitcoin-cli getrawtransaction {x} true"

stdin, stdout, stderr = ssh.exec_command(command2)
lines = stdout.readlines()
error = stderr.readlines()


def equal(x):
    if len(lines) == 0:
        return False
    z = lines[1]
    z = z[10:-2]
    if z in x:
        return "Your transaction is in the mempool"
    else:
        return False

print(equal(x))

command3 = "docker exec bitcoin bitcoin-cli getrawmempool true"


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)


stdin, stdout, stderr = ssh.exec_command(command3)
lines = stdout.readlines()
#print(lines)
#print(type(lines))

# Get user input of transaction

# Parses through mempool returning index of txid in mempool list
def mempool_parser(x):
    y = 0
    for z in lines:
        if x in z:
            return y
        y += 1


y = mempool_parser(x)
#print(mempool_parser(x))


# Slice tx data from mempool list
tx_data = lines[y:y+27]
#print(tx_data)

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
print("vsize = " + str(vsize))
print("fees = " + format(fee,'.00000000f'))
print("sats/vbyte = " + format(sats_per_vbyte, 'f'))
print("\n")


# print("Your TXID is" + x)

del stdin
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

# print("Your TXID is" + x)

del stdin
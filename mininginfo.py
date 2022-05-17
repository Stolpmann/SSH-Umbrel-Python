import paramiko

host = "umbrel.local"
port = 22
username = "umbrel"
password = "123Blizzard!"

command = "docker exec bitcoin bitcoin-cli getmininginfo"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)


stdin, stdout, stderr = ssh.exec_command(command)
lines = stdout.readlines()



blocks = lines[1]
x = lines[2]
# function for rounding hashrate

def hash_rounder():
    z = x.split()
    z = z[1]
    z = z[:-4]
    if len(z) > 10:
        z = z[:-10]
        z = z[:2] + '.' + z[2:]
        return z + ' TH/s'
    else:
        return False


j = hash_rounder()
print(j)

print(blocks)
print(lines)

del stdin
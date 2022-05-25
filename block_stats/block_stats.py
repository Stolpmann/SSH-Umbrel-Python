import paramiko
import secrets
import pandas as pd


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

avgfee = []
avgfeerate = []
avgtxsize = []
blockhash = []
height = []
ins = []
maxfee = []
maxfeerate = []
maxtxsize = []
medianfee = []
mediantime = []
mediantxsize = []
minfee = []
minfeerate = []
mintxsize = []
outs = []
subsidy = []
swtotal_size = []
swtotal_weight = []
swtxs = []
time = []
total_out = []
total_size = []
total_weight = []
totalfee = []
txs = []
utxo_increase = []
utxo_size_inc = []

def scraper():
    # stats = """'["totalfee","avgfeerate", "avgfee" ]'"""
    x = 1

    while x < 5000:
        command2 = f"docker exec bitcoin bitcoin-cli getblockstats {x}"
        stdin, stdout, stderr = ssh.exec_command(command2)
        blockstats = stdout.readlines()
        avgfee.append([blockstats[1]])
        avgfeerate.append([blockstats[2]])
        avgtxsize.append([blockstats[3]])
        blockhash.append([blockstats[4]])
        height.append([blockstats[12]])
        ins.append([blockstats[13]])
        maxfee.append([blockstats[14]])
        maxfeerate.append([blockstats[15]])
        maxtxsize.append([blockstats[16]])
        medianfee.append([blockstats[17]])
        mediantime.append([blockstats[18]])
        mediantxsize.append([blockstats[19]])
        minfee.append([blockstats[20]])
        minfeerate.append([blockstats[21]])
        mintxsize.append([blockstats[22]])
        outs.append([blockstats[23]])
        subsidy.append([blockstats[24]])
        swtotal_size.append([blockstats[25]])
        swtotal_weight.append([blockstats[26]])
        swtxs.append([blockstats[27]])
        time.append([blockstats[28]])
        total_out.append([blockstats[29]])
        total_size.append([blockstats[30]])
        total_weight.append([blockstats[31]])
        totalfee.append([blockstats[32]])
        txs.append([blockstats[33]])
        utxo_increase.append([blockstats[34]])
        utxo_size_inc.append([blockstats[35]])

        x += 1


scraper()

df = pd.DataFrame(list(zip(avgfee,avgfeerate,avgtxsize,blockhash,height,ins,maxfee,maxfeerate,
                           maxtxsize,medianfee,mediantime,mediantxsize,minfee,minfeerate,
                           mintxsize,outs,subsidy,swtotal_size,swtotal_weight,swtxs,time,
                           total_out,total_size,total_weight,totalfee,txs,utxo_increase,
                           utxo_size_inc,)),
               columns =['avgfee', 'avgfeerate', "avgtxsize", "blockhash",
                         "height", "ins", "maxfee", "maxfeerate", "maxtxsize",
                         "medianfee", "mediantime", "mediantxsize", "minfee",
                         "minfeerate", "mintxsize", "outs", "subsidy", "swtotal_size",
                         "swtotal_weight", "swtxs", "time", "total_out", "total_size",
                         "total_weight", "totalfee", "txs", "utxo_increase", "utxo_size_inc"])

# print(df[['avgfee', 'avgfeerate', "avgtxsize", "blockhash",
#                          "height", "ins", "maxfee", "maxfeerate", "maxtxsize",
#                          "medianfee", "mediantime", "mediantxsize", "minfee",
#                          "minfeerate", "mintxsize", "outs", "subsidy", "swtotal_size",
#                          "swtotal_weight", "swtxs", "time", "total_out", "total_size",
#                          "total_weight", "totalfee", "txs", "utxo_increase", "utxo_size_inc"]])

df.to_csv('mining/blockchain_data.csv', index=False)


del stdin
import re
regrex_format = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

string = 'Aug 24 03:57:28 localhost sshd[18416]: Failed password for root from 202.109.143.35 port 3852 ssh2'

lol = re.findall(string=string, pattern=regrex_format)

print(lol[0])

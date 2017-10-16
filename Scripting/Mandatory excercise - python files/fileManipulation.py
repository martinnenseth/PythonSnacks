import argparse
import re
import os

regrex_ip = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
regrex_port = '(?<=port )\d*'
# task 1
parser = argparse.ArgumentParser(description="Attack file")
parser.add_argument('--filename')
parser.add_argument('--start')
parser.add_argument('--end')
args = parser.parse_args()
print('argssss', args.start, args.end)

lines = []
usernames = []
occurences = {}
unique_usernames = []
hashmap_dict = {}
ipsStored = []
occurences_ips = {}
unique_ips = []
final_ip = []
ip_and_port = []

def init():
    with open(args.filename) as file:
        # task 2
        for line in file:
            lines.append(str(line))
            # task 6
            final_ip.extend(get_ip_amount_attack(line))

            # task 7
            ip_and_port.extend(get_ip_and_port(line))


            # task 3
            if line.__contains__("Invalid user"):
                username = line.split("user", 1)[1]
                # remove space before username
                username = username.split(" ", 1)[1]
                username = username.split(' ', 1)[0]
                usernames.append(username)

        # task 3 output
        print(usernames)


    # task 4
def count_occurence():
    for user in usernames:
        hashmap_dict[hash(user)] = user # task 5
        occurences[user] = usernames.count(user)
        # Find unique usernames
        if usernames.count(user) == 1:
            unique_usernames.append(user)

        print("number of times each username has been used", occurences)
        print(" ")
        print(" ")
        print("unique usernames: ", unique_usernames)
        print(" ")
        print(" ")
        print("task 5, hashma-type dictionary", hashmap_dict)


def get_ip_and_port(line):
    ips_port = []
    ips_g =[]

    ips = re.findall(string=line, pattern=regrex_ip)
    ports = re.findall(string=line, pattern=regrex_port)
    if len(ips) > 0:
        for i in range(len(ips)):
            try:
                ips_port.append({'ip': ips[i], 'port': ports[i]})
            except:
                ips_port.append({'ip': ips[i], 'port': 'none'})
            ips_g.extend(ips)

    return ips_port


def get_ip_amount_attack(line):

    ips_g = []

    ips = re.findall(string=line, pattern=regrex_ip)
    if len(ips) > 0:
        for i in range(len(ips)):
            ips_g.extend(ips)


    unique_ips = list(set(ips_g))
    final_ip = []
    for ip in unique_ips:
        final_ip.append({'ip': ip, 'amount': ips_g.count(ip)})

    return final_ip


#task 7
def scan():
    selected_ips = []
    for x in ip_and_port:
        if x['port'] != 'none':
            if x['port'] >= args.start and x['port'] <= args.end:
                selected_ips.append(x['ip'])
                print(x)

    return selected_ips


# task 8
def ping_selected_ips(selected):
    answered = []
    selected = list(set(selected))      # remove dublicates

    for i in selected :
        if os.system('ping -c 1 {}'.format(i)) == 0 :
            answered.append(i)

    return answered

init()
count_occurence()
f = open('ip_responded', 'w+')

for i in ping_selected_ips(scan()):
    write = True
    for line in f:
        if line == i:
            write = False
            break
    if write :
        f.writelines(i)
f.close()



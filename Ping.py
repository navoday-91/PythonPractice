import subprocess
from operator import itemgetter
#ip addresses and regions in same sequence
ipaddresses = ["23.23.255.255", "13.56.63.251", "34.240.0.253", "34.208.63.251"]
regions = ["US East", "US West", "EU     ", "Oregon "]
latencylist = []
i=0
#lopping through all ip addresses in list
for host in ipaddresses:
    ping =subprocess.Popen(
        ["ping", "-c", "3", host],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )
    out, error = ping.communicate()
    print(out)
    #Making an o/p list of tuples - [(avg latency, ip address, region)...(,,)]
    latencylist.append((float(str(out).split("min/avg/max/stddev = ")[1].split("/")[1]), host, regions[i]))
    i+=1

#sorting for average latency 
latencylist.sort(key=itemgetter(0))

for results in latencylist:
    print(results[2] + "    "+ results[1] + "    " + str(results[0]))





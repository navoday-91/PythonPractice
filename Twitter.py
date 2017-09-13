import json
from collections import defaultdict
from datetime import datetime

url = "/Users/navodaytomar/Library/Containers/com.apple.mail/Data/Library/Mail Downloads/09C4A784-038F-45EA-B9E7-EAFB4C8\
041AF/Twitter Storage SRE Coding Challenge/responses.txt"
outfile = "/Users/navodaytomar/OutFile.txt"
t1 = datetime.now()
with open(url, 'r') as f:
    responsetxt = f.read()
    jsonresp = json.loads(responsetxt)
responsedct = defaultdict(list)
for jsonrespitem in jsonresp:
    Success_Rate = (jsonrespitem['Success_Count'] / jsonrespitem['Request_Count']) * 100
    responsedct[jsonrespitem['Application'] + ' ' + jsonrespitem['Version']].append(Success_Rate)
result = {}
line_num = 1
jsonout = []
print('App    ' + 'Ver   ' + 'Succ_Rate')
print('_______________________\n')
for dictitem, rates in sorted(responsedct.items()):
    Success_Rate = sum(rates) / len(rates)
    Success_Rate = round(Success_Rate, 2)
    Appdetails = dictitem.split()
    jsondict = {'Application': Appdetails[0], 'Version': Appdetails[1], 'Success_Rate': Success_Rate}
    jsonout.append(jsondict)
    if line_num == len(responsedct):
        print(dictitem + ' ' + str(Success_Rate))
    else:
        print(dictitem + ' ' + str(Success_Rate) + '\n')
    line_num += 1
with open(outfile, 'w') as output:
    json.dump(jsonout, output)
t2 = datetime.now()
print(t2 - t1)

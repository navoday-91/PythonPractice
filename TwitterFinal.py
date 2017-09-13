import json
from syncasync import get
from collections import defaultdict

# This is prefix path to the endpoints mentioned in Servers.txt file
serverurl = "https://abc/xyz/"
# Path to Servers.txt file
endpoints = "/Users/navodaytomar/Library/Containers/com.apple.mail/Data/Library/Mail Downloads/09C4A784-038F-45EA-B9E7-E\
EAFB4C8041AF/Twitter Storage SRE Coding Challenge/servers.txt"
# Path for Output file written with aggregate Success Rate for Applications and Versions
outfile = "/Users/navodaytomar/Library/Containers/com.apple.mail/Data/Library/Mail Downloads/09C4A784-038F-45EA-B9E7-EAF\
EAFB4C8041AF/Twitter Storage SRE Coding Challenge/OutFile.txt"
# Read servers.txt file and store them in a list
with open(endpoints, 'r') as sf:
    server_endpoints = sf.read().splitlines()
# responsedct is a dictionary where value corresponding to a key is a 'List'
responsedct = defaultdict(list)
# For every endpoint from servers.txt file : build the url with prefix path and read the response in json format
for endpointurl in server_endpoints:
    responsetxt = get(endpointurl)
    jsonresp = json.loads(responsetxt)
    # for all unique App + Ver keys, store their success rates from each record retrieved in response
    for jsonrespitem in jsonresp:
        Succ_Rate = (jsonrespitem['Success_Count'] / jsonrespitem['Request_Count']) * 100
        responsedct[jsonrespitem['Application'] + ' ' + jsonrespitem['Version']].append(Succ_Rate)
# Calculate aggregate success rate by computing average of all success rates against an app & ver
# Write the result json to stdout and output file (Note - Last record should not contain a new line char at end)
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

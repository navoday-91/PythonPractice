dict1 = set([('a',10,20), ('c',15,25), ('b',5,10), ('d',20,30), ('f',30,35), ('g',25,45), ('e',45,60), ('h',22,32)])

#method 2 using sorted only (will have to pass a key in else which will pull the unmatched items to bottom in sort
# I don't like this method much
dict1 = sorted(dict1, key = lambda elem: (elem[1], elem[2], elem[0]))
query = 25
crawl = False
a = 0
b = len(dict1) - 1
while  a<=b:
    if crawl:
        i += 1
        if dict1[i][1] > query or i == len(dict1):
            b = i - 1
            break
    else:
        i = (a + b) // 2
        if dict1[i][1] > query:
            b = i-1
        elif dict1[i][1] < query:
            a = i+1
        else:
            crawl = True
end = b
a = 0
while  a<=b:
    if crawl:
        i -= 1
        if dict1[i][2] < query or i == -1:
            a = i + 1
            break
    else:
        i = (a + b) // 2
        if dict1[i][2] > query:
            b = i-1
        elif dict1[i][2] < query:
            a = i+1
        else:
            crawl = True
start = a
print(dict1)
print("Query :" + str(query))
print([dict1[i] for i in range(start,end+1)])
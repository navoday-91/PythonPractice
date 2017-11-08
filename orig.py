def orignial(input1):
    s= input1[0:1]
    for i in range(1, len(input1), 2):
        s += input1[i:i+1]
    s = s[::-1]
    for i in range(2,len(input1),2):
        s += input1[i:i+1]
    if len(input1) % 2 == 0:
        return s[::-1]
    else:
        return s

def revert(s1):
    o1 = o2 = ''
    i = len(s1)-1
    while i >= 0:
        o2 += s1[i]
        i -= 1
        o1 += s1[i]
        i -= 1
    return o1+o2
print(orignial('cdbeaf'))
print(orignial('cbdae'))
print(revert('cdbeaf'))
print(revert('cbdae'))



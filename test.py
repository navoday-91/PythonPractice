l = [2,6,4,3,11,7]
limit = 12
l = sorted(l)
b = j = len(l)-1
a = i = 0
grtr = lesser = False
print(l)
while True:
    print("running index:",i,j)
    if l[i] + l[j] > limit:
        if lesser == True:
            i -= 1
            break
        j -= 1
        grtr = True
    elif l[i] + l[j] < limit:
        i += 1
        lesser = True
    else:
        break
print("answer :",l[i],l[j])



def cyclicSequence(s):
    a = i = s.index(min(s))
    while (a+1)%len(s) != i:
        if s[a] >= s[(a+1)%len(s)]:
            return False
        a = (a+1)%len(s)
    return True
print(cyclicSequence([1,1]))


print(11%7)
print(121%7)
print((121*11)%7)
print((13*19)%7)

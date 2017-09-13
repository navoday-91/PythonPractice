primeBinaryDigitSum = lambda s,e,t: [n for n in range(max(2,s), e+1) if bin(n).count('1') == t and not any(y for y in range(2,1+int(n**.5))
if not n%y)]
print(primeBinaryDigitSum(1,(2**31)-1,15))
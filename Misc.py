import base64 as t

base64replace = lambda a, b, c: str(a.replace(str(t.b64encode(b.encode()))[2:-1], str(t.b64encode(c.encode()))[2:-1]))

u = "SGksIEV2ZXJ5b25lIQ=="
v = "Hi"
w = "Okay"

print(base64replace(u,v,w))

print(t.b64encode(v.encode()))
print(t.b64encode(w.encode()))



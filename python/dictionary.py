#lesson 5 about dictionary
a={}
a["one"]="unu"
a["one"]="cat"
a["two"]="doi"
a["three"]="trei"

print(a)

for e,v in a.items():
    print (e+","+v)

print("***")

for e in a:
    print (e,a[e])

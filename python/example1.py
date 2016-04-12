#dictionary literal similar to associative arrays
#the key is integer and the value is list
d={1:["a","b","c"],2:["potato","salad"],3:["viena","paris"]}

print (d[1])
print (d[2])
print (d[3])

#nested loops
print("loop starts")
for e,v in d.items():
    print("e=",e)
    print("v=",v)
    for c in v:
        print ("   c=",c)
    #end for
#end for

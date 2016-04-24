import random

mylist = []

for somethin in range(1,10):
    x = random.randrange(0,9)
    mylist.append(x)

print(mylist)


last_index=len(mylist)
print ("length of mylist is:",len(mylist))
print ("first element is:",mylist[0])
print ("last element is:",mylist[len(mylist)-1])

    
#is mylist sorted?
is_mylist_sorted = False

x=0
y=1
intermediate=None

#how many switches?
number_of_switches = 0

#bubble sort
while not is_mylist_sorted:
    
    if mylist[x] > mylist[y]:
        intermediate=mylist[x]
        mylist[x]=mylist[y]
        mylist[y]=intermediate
        number_of_switches+=1
    x+=1
    y+=1
   
    if y==last_index:
        x=0
        y=1
        
        if number_of_switches==0:
            is_mylist_sorted = True
        else:
            number_of_switches = 0


print("finished")
print("is my list sorted?",is_mylist_sorted)
print("my list",mylist)

    

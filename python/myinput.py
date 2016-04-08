#demo program for master loop

print ("this is my first program")
print ("options: 1,2,3")


n=input(":")
while n != "0":

  if n in ["1","2","3"]:
    print("option is:" + n)
  else:
    print("invalid option:" + n)

  if n=="1":
    print("welcome to arcadia")
  elif n=="2":
    print("welcome to your worst nightmare")
  elif n=="3":
    print("the water is poison")
  else:
    print("error")

  n=input(":")
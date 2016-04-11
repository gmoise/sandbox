#demo of class MyClass
class MyClass:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.skills=["Java","JavaScript","Python"]

    def display(self):
        print("name:"+self.name)
        print("age:"+self.age)
        print("skills:")
        for s in self.skills:
            print (s.rjust(20,"."))
        print ("__________________")


#newinstance n of class MyClass       
n=MyClass("George","22")
m=MyClass("Savannah","88")

#call a method of an object n using name of method followed by ()
n.display()
m.display()

#properties of object are visible outside of class
print (n.name)

#in Python properties of an object are not protected and can be changed
n.name = "Afrika"
print (n.name)
n.display()

#let's make a list of persons
catalog = []
catalog.append(n)
catalog.append(m)
print(catalog)

#print the list of persons
for c in catalog:
    c.display()

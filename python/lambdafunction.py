#simple lambda function with two parameters
f = lambda x,y:x+y

#using lambda function like normal function
print (f(1,2))

#high order function that is using a function as parameter
def hof(func,c,d):
    a=func(c,d)
    return a

result=hof(f,2,3)
resulttwo=hof(lambda x,y:x**2,6,2)
print(result)
print(resulttwo)

bucket=[2,4,6,8]

#list comprehension
test=[x for x in range(0,20)]

#using lambda in map function
maplist=map(lambda x:x+2, test)
print(list(maplist))

#filter function to filter an iterable collection using anonymous function lambdaa
filterlist=filter(lambda x:x%2==0, test)
print(list(filterlist))

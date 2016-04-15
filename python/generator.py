#Create a generator
def test_generator(p_start, p_stop):
    counter = p_start
    while counter <= p_stop:
       yield counter
       counter +=3
 
def main():
    # example generator:"aindex"
    print("call generator using loop")
    aindex = test_generator(1,10)
    print (aindex)
    for i in aindex:
        print("i=%d" % i)
        
    # example generator:"bindex"     
    print("call generator using next")
    bindex = test_generator(3,5)
    print("y=%d" % next(bindex))
    print("y=%d" % next(bindex))
 
# compiler entry point
if __name__ == "__main__":
    main()

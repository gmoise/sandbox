# Create a closure with mutable attribute: index
def test_closure(min,max):
    index = {1:min} #dictionary of one element
    def enclosed():
        if index[1] < max:
           index[1] += 1
           return index[1]
        else:
           raise Exception("error")
           
    return enclosed
 
def main():
    # use closure based function my_scan()
    my_scan = test_closure(100,110);
    for i in range(0,50):
        print(i,'->',my_scan())
 
 
# compiler entry point
if __name__ == "__main__":
    main()

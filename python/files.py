#io is a module for working with text files
import io

#opening a file
file = io.open('file.txt', mode='r')

#reading all lines into list c
c = file.readlines()
print(c)

#jump to the beginning of the file
file.seek(0)

#reading row by row
for row in file:
    print (row)

file.close()

#create a new file for writting into
file = io.open("filetwo.txt", mode='w')

#make a copy by writting line by line
for element in c:
    print(element)
    file.write(element)
file.close()

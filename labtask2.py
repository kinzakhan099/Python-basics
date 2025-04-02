file=open("myfile.txt","w")#creating a new file
file.write("\nThis is my first file.\nIn this file, we will talk about file handling.\n it is very interesting topic.")
file.close()#closing the file

file=open("myfile.txt","r")#open the file in read mode
content=file.read()#reading the content of the file
print("\nBefore appending, File content is: ",content)#printing the content of the file
file.close()#closing the file

file=open("myfile.txt","a")
file.write("\nFile is a collection of related data stored on a permanent basis in the computer.\n")
file.close()

file=open("myfile.txt","r")#open the file in read mode
content=file.read()#reading the content of the file     
print("\nAfter appending, File content is: ",content)#printing the content of the file
file.close()#closing the file
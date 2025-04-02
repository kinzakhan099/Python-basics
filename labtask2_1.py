#creating a new text file and writing three lines of text to it
with open("myfile2.txt", "w") as file:
    file.write("this is python file\n")
    file.write("we'll talk about file handling in it.")
    file.write("file handling is very important.\n")

#reading the content of the file and displaying it
with open("myfile2.txt", "r") as file:
    content=file.read()
    print("File Content After Writing:")
    print(content)

#appending a new line to the file
with open("myfile2.txt", "a") as file:
    file.write("file handling can be done in many ways.\n")
    file.write("there are many functions available for file handling.\n")
    file.write("we'll discuss them in detail.\n")

#reading the updated content of the file and displaying it
with open("myfile2.txt", "r") as file:
    updated_content=file.read()
    print("File Content After Appending:")
    print(updated_content)
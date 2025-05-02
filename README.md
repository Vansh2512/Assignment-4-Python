# Assignment-4-Python

 
Task 1: Read a File and Handle Errors 
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.

#Logic to solve:

try:

This means: "Try to do something that might cause an error."

We’re going to try opening and reading the file.

with open('Assignment 4/sample.txt','r') as file1:

This tries to open the file located in the folder Assignment 4 named sample.txt.

'r' means we are opening it in read mode.

with makes sure the file is automatically closed after reading.

file1.read()

This reads the entire content of the file.

print(file1.read()) will display all the text inside the file.

except FileNotFoundError:

If Python cannot find the file, it will skip the try block and go here.

FileNotFoundError is a specific error that happens when a file doesn’t exist.

print("Error: The file 'sample.txt' was not found")

This shows a clear error message if the file is missing

###########################################################################################

Task 2: Write and Append Data to a File
 
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.

#Logic to solve:

Writes to a file
'w' mode means write — it erases old data and writes new.

User enters some text.

That text is saved into the file output.txt.

File is closed after writing.

Appends new text
'a' mode means append — it adds text to the end of the file.

'\n' + input2 means it adds a newline before writing the new text.

File is closed after appending.

Reads and displays the content
'r' mode is for reading the file.

It prints all text stored in the file.

File is closed after reading.

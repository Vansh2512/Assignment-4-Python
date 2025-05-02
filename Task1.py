try:
   with open('Assignment 4/sample.txt','r') as file1:
       print(file1.read())
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found")


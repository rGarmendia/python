# file = open("fruits.txt")
# content = file.read()
# file.close()
# print(len(content))

def find_in_file():
    myfile = open("fruits.txt")
    fruits = myfile.read()
    fruits = fruits.splitlines()
    for fruit in fruits:
        print(len(fruit)) 

find_in_file()

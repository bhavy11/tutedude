with open('Output.txt', "r+") as Output:
    write_Output = Output.write("Hello, python!")
    print(write_Output)
with open('Output.txt', "a") as Output:
    append_Output = Output.write("Learning file handling in python.")
    print(append_Output)
with open('Output.txt', "r") as Output:
    num=int(input("Enter number: "))
    read_Output = Output.read(num)
    print(read_Output)
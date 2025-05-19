try:
    mydict={'alex':90, 'Alice':85, 'hero':70}
    a=str(input("Enter the student's name: " ))
    print(mydict[a])
except KeyError:
    print("Student not found")
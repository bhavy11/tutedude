try:
    with open('sample.txt',"r")as sample:
        read_sample = sample.read()
        print(read_sample)
except IndentationError:
    print("error: File 'sample.txt' is not found")
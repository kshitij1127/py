def calclimit():
    wordlimit = 10
    numwords = 0
    filename = input("Enter the filename: ")
    filename = open(filename, "r")

    for line in filename:
        words = line.split()
        numwords = numwords + len(words)
        

    if numwords > wordlimit:
        print("uh oh, you have exceeded the word limit")
    else:
        print("you have not exceeded the word limit")    
    

calclimit()
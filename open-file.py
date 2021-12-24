def countwords():
    filename = input("Enter a file name: ")
    numwords = 0
    file = open(filename, 'r')
    for line in file:
        words = line.split()  # split line into words
        numwords += len(words) # add number of words from each line to numwords
    
    print("There are", numwords, "words in", filename)


countwords()
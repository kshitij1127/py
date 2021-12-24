def swap():
    data_a = input("Enter a file name: ")
    data_b = input("Enter a file name to swap: ")

    with open(data_a, 'r') as f:
        data_1 = f.read()

    with open(data_b, 'r') as f:
        data_2 = f.read()

    with open(data_a, 'w') as f:
        f.write(data_2)
        
    with open(data_b, 'w') as f:
        f.write(data_1)

swap()
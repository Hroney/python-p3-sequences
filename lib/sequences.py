def print_fibonacci(length):
    if (length == 0):
        print([])
        return []
    if (length == 1):
        print([0])
        return [0]
    if (length == 2):
        print([0,1])
        return [0,1]
    arr = [0,1,1]
    num1 = 1
    num2 = 1
    tempnum = 0
    while (len(arr) < length):
        tempnum = num1 + num2
        arr.append(tempnum)
        num1 = num2
        num2 = tempnum
    print(arr)
    return arr
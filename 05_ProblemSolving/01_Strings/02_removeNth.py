def removeNth(string, n):
    first = string[:n]
    last = string[n+1:]

    return first + last

string = str(input("Enter string: "))
n = int(input("Enter nth index to remove character: "))
print(removeNth(string, n))
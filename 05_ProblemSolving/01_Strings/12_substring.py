def subString(str1, sub1):
    if sub1 in str1:
        print("substring found")
    else:
        print("sub string not found")

str1 = input("Enter full string: ")
sub1 = input("Enter sub string: ")
subString(str1, sub1)

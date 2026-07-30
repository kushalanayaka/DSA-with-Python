def oddIndex(str1):
    res = ""
    for i in range(len(str1)):
        if i % 2 == 0:
            res = res + str1[i]
    return res

str1 = str(input("Enter string: "))
print(oddIndex(str1))


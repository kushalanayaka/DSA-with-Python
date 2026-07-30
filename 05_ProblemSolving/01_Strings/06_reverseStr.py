def reverseStr(str1):
    #rev = str1[::-1]
#--------------------------------------
    rev = ""
    for i in str1:
        rev = i + rev
    return rev

str1 = input("Enter a word: ")
print(reverseStr(str1))
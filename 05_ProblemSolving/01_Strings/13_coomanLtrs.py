def commonLetters(str1, str2):
    a  = list(set(str1)|set(str2))
    for i in a:
        print(i)

str1 = input("Enter string1: ")
str2 = input("Enter string2: ")
commonLetters(str1, str2)
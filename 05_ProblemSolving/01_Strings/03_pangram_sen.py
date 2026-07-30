from string import ascii_lowercase
def pangram(str1):
    
    #return set(ascii_lowercase).issubset(str1.lower())
    #----------------------------------------------------------------
    return len(set(c.lower() for c in str1 if str1.isalpha())) == 26

str1 = str(input("Enter a String: "))
print(pangram(str1))

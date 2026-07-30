def lowerCase(text):
    count = 0
    #for i in text:
    #   if i.islower():
    #       count = count + 1
#-------------------------------------------
    for ch in text:
        if ch >= 'a' and ch <= 'z':
            count += 1

    print(f"the sentace conatins {count} lower case characters")

text = input("Enter a sentace: ")
lowerCase(text)
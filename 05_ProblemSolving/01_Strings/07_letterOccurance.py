def letterOccurance(str1, ch):
    count = 0
    for i in str1:
        if i == ch:
            count = count + 1

    return f"{ch} is apperred {count} times"

str1 = str(input("enter a word: "))
ch = input("enter a character: ")
result = letterOccurance(str1, ch)
print(result)
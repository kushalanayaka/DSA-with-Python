def vowelCount(text):
    count = 0
    li = []
    for i in text.lower():
        if i in "aeiouAEIOU":
            li.append(i)
            count += 1

    print(f"{count} vowels and {set(li)} are vowels")

text = input("enter a string: ")
vowelCount(text)
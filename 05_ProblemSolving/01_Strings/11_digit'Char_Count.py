def digitChar(text):
    count1 = 0
    count2 = 0
    for i in text:
     #   if i.isdigit():
      #      count1 += 1
       # else:
        #    count2 += 1
#-------------------------------------------
        if i.isalpha():
            count2 += 1
        elif i.isdigit():
            count1 += 1

    print(f"{count1} digits and {count2} characters")

text = input("Enter a sentance with digits and characters: ")
digitChar(text)
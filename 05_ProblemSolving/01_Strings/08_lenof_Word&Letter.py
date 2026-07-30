def lengthWO(text):
    #w_count = len(text.split())
    #l_count = len(text.replace(" ", ""))

    #print(f"The sentance consist {w_count} words")
    #print(f"The sentance consist {l_count} letters")
#---------------------------------------------------------------
    w_count  = 0
    l_count = 0
    in_word = False

    for ch in text:
        if ch != ' ':
            l_count = l_count + 1

        if ch != ' ' and in_word == False:
            w_count = w_count + 1
            in_word = True
        elif(ch ==' '):
            in_word = False


    print(f"The sentance consist {w_count} words")
    print(f"The sentance consist {l_count} letters")


text = str(input("Enter a sentace : "))
lengthWO(text)

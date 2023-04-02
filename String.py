try:
    row = input("Enter the row: ")
    search_word = input("Enter the searth world: ")
    replace_word = input("Enter the replace world: ")

    words = row.split()

    for i in range(len(words)):
        if words[i] == search_word:
            words[i] = replace_word

    new_row = ' '.join(words)
         
    print("Received row: ", new_row)
except Exception as ex:
    print(ex)
finally:
    print("Exit")


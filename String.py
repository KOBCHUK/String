try:
    row = input("Enter the row: ")
    search_word = input("Enter the searth world: ")
    replace_word = input("Enter the replace world: ")

    words = row.split()
    new_text = ""

    for word in words:
        if word == search_word:
         new_text += replace_word + " "
        else:
         new_text += word + " "

    print("Received row: ", new_text.strip())
except Exception as ex:
    print(ex)
finally:
    print("Exit")


try:
    row = input("Enter the row: ")
    search_word = input("Enter world: ")
    row = row.lower()
    count = 0
    words = row.split()

    for word in words:
        if word == search_word:
            count += 1

    print("The world '{}' occurs {} items in the line.".format(search_word, count))
except Exception as ex:
    print(ex)
finally:
    print("exit")

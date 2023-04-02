try:
    import re
    text = input("Enter the row: ")
    search_word = input("Enter the search world: ")
    delimiters = [' ', ',', '.', ';', ':', '-', '?', '!', '(', ')', '\n']
    count = 0

    words = re.split('|'.join(map(re.escape, delimiters)), text)

    for word in words:
        if word == search_word:
            count += 1

    print("The world \"{}\" occurs {} item in the line.".format(search_word, count))
except Exception as ex:
    print(ex)
finally:
    print("Exit")
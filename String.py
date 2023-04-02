try:
    row = input("Enter a row: ")
    char = input("Enter a character: ")

    row = row.lower()

    count = row.count(char)

    print(f"The character '{char}' occurs {count} times in the row.")

except Exception as ex:
    print(ex)
finally:
    print("exit")


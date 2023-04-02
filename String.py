try:
    row = input("Enter a row: ")
    reversed_row = row[::-1]
    print("Reversed row:", reversed_row)
except Exception as ex:
    print(ex)
finally:
    print("Exit")

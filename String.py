try:
    row = input("Enter the row: ")
    letters = 0
    numbers = 0

    for char in row:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            numbers += 1

    print("Letters:", letters)
    print("Numbers:", numbers)
except Exception as ex:
    print(ex)
finally:
    print("Exit")
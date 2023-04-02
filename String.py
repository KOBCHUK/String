try:
    row = input("Enter the row: ")
    world = input ("Enter the world: ")
    row = row.lower()
    row_1 = row.split()
    print(row_1)
    count = row_1.count(world)

    print (f"The world '{world}' occurs {count} times in the row")
except Exception as ex:
    print(ex)
finally:
    ("Exit")

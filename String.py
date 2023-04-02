try:
    row = input("Enter the row: ")
    world = input ("Enter the world: ")
    row = row.lower()
    row = row.split()
   
    count = row.count(world)

    print (f"The world '{world}' occurs {count} times in the row")

except Exception as ex:
    print(ex)
finally:
    ("Exit")

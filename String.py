try:
    row = input("Enter the row: ")
    world = input ("Enter the world: ")
    
    count = row.count(world)

    print (f"The world '{world}' occurs {count} times in the row")
except Exception as ex:
    print(ex)
finally:
    ("Exit")

try:
    row = input("Enter the row: ")
    world_1 = input("Enter the world_1: ")
    world_2 = input("Enter the world_2: ")
    new_row = row.replace(world_1, world_2)
    print(f"The resulting line is: {new_row}")
except Exception as ex:
    print(ex)
finally:
    print("exit")


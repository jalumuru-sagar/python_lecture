choice=int(input("Enter 1 for AND, 2 for OR, 3 for NOT: "))

match choice:
    case 1:
        print("AND")
    case 2:
        print("OR")
    case 3:
        print("NOT")
    case _:
        print("INVALID CHOICE")
choice=input("Enter a Traffic Light Color (Red/Yellow/Green/orange): ").strip().lower()

match choice:
    case "red":
        print("STOP")
    case "yellow" | "orange":
        print("PREPARE TO STOP")
    case "green":
        print("GO")
    case _:
        print("INVALID CHOICE")
     
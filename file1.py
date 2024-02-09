n = str(input("Son kiriting: "))
if n.isdigit():
    match len(n):
        case 1:
            print("Bir xonalik son!!!")
        case 2:
            print("Ikki xonalik son!!!")
        case 3:
            print("Uch xonalik son!!!")
        case 4:
            print("To'rt xonalik son!!!")
        case 5:
            print("Besh xonalik son!!!")
        case 6:
            print("Olti xonalik son!!!")
        case _:
            print("Max 6 xonalik son!!!")
else:
    print("Raqam kiriting!!!")
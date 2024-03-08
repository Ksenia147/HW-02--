print ("Добро пожаловать в игру крестики-нолики!\n"
       "Чтобы сделать ход введите координаты Х Y через пробел\n"
       "    Х - номер строки\n"
       "    Y - номер столбца")
count = 0
field = [["-"] * 3 for i in range(3)]
wins = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
def win():
    for cord in wins:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            playing_field()
            print("Выиграл X!")
            return True
        if symbols == ["0", "0", "0"]:
            playing_field()
            print("Выиграл 0!")
            return True
    return False
def playing_field():
    print("    0 1 2")
    for i, row in enumerate(field):
        row_str = f" {i}  {' '.join(row)} "
        print(row_str)

while True:
    playing_field()
    if count % 2 == 0:
        motion = input("Ходит Х, введите координаты: ").split()
    else:
        motion = input("Ходит 0, введите координаты: ").split()
    if len(motion) != 2:
        print(" Введите 2 координаты! ")
        continue
    x, y = motion
    if not(x.isdigit()) or not(y.isdigit()):
        print("Введите числа!")
        continue
    x, y = int(x), int(y)
    if 0 > x or x > 2 or  0 > y or  y > 2:
        print("Координаты вне диапазона!")
        continue
    if field[y][x] != "-":
        print(" Клетка занята! ")
        continue
    if count % 2 == 0:
        field[y][x] = "X"
    else:
        field[y][x] = "0"
    count += 1
    if win():
        break
    if count == 9:
        print("Ничья!")
        break

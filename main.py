'''
# Функция для проверки выигрыша
def check_winner(board):
    # Проверяем строки
    for row in board:
        if row.count('X') == 3 or row.count('O') == 3:
            return True
    # Проверяем столбцы
    for i in range(3):
        col = [board[j][i] for j in range(3)]
        if col.count('X') == 3 or col.count('O') == 3:
            return True
    # Проверяем диагонали
    diag1 = [board[i][i] for i in range(3)]
    if diag1.count('X') == 3 or diag1.count('O') == 3:
        return True
    diag2 = [board[i][2 - i] for i in range(3)]
    if diag2.count('X') == 3 or diag2.count('O') == 3:
        return True
    return False
'''

def drow_area():
    for i in area:
        print(*i)
    print()

area =[['*','*','*'] , ['*','*','*'] , ['*','*','*']]
print('Давайте сыграем в крестики нолики:')
print('----------------------------------')
drow_area()
for turn in range (1 , 10):
    print(f'Ход  : {turn}')
    if turn % 2 == 0:
        turn_char = "0"
        print("Ход второго игрока")
    else:
        turn_char = 'Х'
        print("Ход первого игрока")

    row = int (input('Введите номер по горизонтале (1 ,2,3,): ')) -1
    column = int (input('Введите номер по вертикале (1 ,2,3,): ')) -1
    if  area [row] [column] =='*':
        area [row] [column] = turn_char
    else:
        print('Ячейка занята , Вы пропускаете ход! ')
        continue
    drow_area()
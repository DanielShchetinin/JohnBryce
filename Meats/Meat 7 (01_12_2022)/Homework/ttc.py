def board_system():
    board_system = []
    
    for i in range(1, size+1):
        board_system.append(i)

count = 1
a = ' . '
size = int(input("Enter a size: "))

first = True
sizenum = '   '

def board(a, count, size, first, sizenum):
    for idx in range(1, size+1):
        board_1 = ("\n┏" + ((size-1) * "━━━┳") + "━━━┓")
        board_2 = (size * f"┃ {idx} " + "┃")
        board_3 = ("┣" + ((size-1) * "━━━╋") + "━━━┫")
        board_4 = (size * f"┃ {idx} " + "┃")
        board_5 = ("┗" + ((size-1) * "━━━┻") + "━━━┛")
    
    for i in range(1, size+1):
        if first is True:
            print("  ", end = '')
            first = False
        if i >= 9:
            sizenum = ' x '
        print(i, end = sizenum)

    
    
    
    print(board_1)
    while True:
        print(board_2)
        print(board_3)
        count += 1
        if count >= size:
            break
    print(board_4)
    print(board_5)
    
board(a, count, size, first, sizenum)
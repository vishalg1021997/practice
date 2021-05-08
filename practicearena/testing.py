def show_seats(row,col):
    matrix = []
    for i in range(row):
        a = []
        for j in range(col):
            a.append("S")
        matrix.append(a)
    print(end = "  ")
    for j in range(col):
        print( j + 1, end=" ")
    print()
    for i in range(row):
        print(i + 1, end=" ")
        for j in range(col):
            print( matrix[i][j], end=" ")
        print()
    de = int(input())
    fg = int(input())
    print(matrix.index(de,fg))

print(show_seats(7,8))


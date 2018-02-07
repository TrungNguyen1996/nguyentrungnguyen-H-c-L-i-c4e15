print("*" * 5) # hơi hạn chế vì còn có chẵn lẻ nên sẽ dùng vòng lặp

col = int(input("Enter colums: "))
row = int(input("Enter row: "))
for y in range(row):
    for x in range(col):
        if (x + y) % 2 == 0:
            print("x", end=" ")
        else:
            print(" ", end=" ")
    print()

def luckyNumbers(matrix: list[list[int]]):

    luckNum = 0

    for row in matrix:
        min_row = min(row)
        index_min_row = row.index(min_row)
        # Check if is the max value in the column
        max_column = 0
        for i in range(len(matrix)):
            if matrix[i][index_min_row] > max_column:
                max_column = matrix[i][index_min_row]
        if max_column == min_row:
            luckNum = max_column

    return luckNum


print(luckyNumbers([[3, 7, 8], [9, 11, 13], [15, 16, 17]]))
print(luckyNumbers([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]))
print(luckyNumbers([[7, 8], [1, 2]]))

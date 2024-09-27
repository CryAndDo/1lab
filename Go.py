#1
array = (1, 5, 3, 7, 15, 9, 10)
count_5 = array.count(5)
count_15 = array.count(15)
if count_5 == 1 and count_15 == 1:
    index_5 = array.index(5)
    index_15 = array.index(15)
    result = tuple(
        200 if x == 5 else (15 if x == 15 else x) for x in array
    )
    result = tuple(
        (15 if x == 5 else (5 if x == 15 else x)) for x in result
    )
else:
    result = array
print("Обновленный кортеж:", result)

#2
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
max_value = float('-inf')
max_row_index = -1
min_value = float('inf')
min_col_index = -1

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
            max_row_index = i
        if matrix[i][j] < min_value:
            min_value = matrix[i][j]
            min_col_index = j

max_row = matrix[max_row_index]
min_col = tuple(matrix[i][min_col_index] for i in range(len(matrix)))
scalar_product = sum(max_row[k] * min_col[k] for k in range(len(max_row)))
print("Скалярное произведение:", scalar_product)

#3
numbers = [5, 10, 20, 15, 20, 30]
for i in range(len(numbers)):
    if numbers[i] == 20:
        numbers[i] = 200
        break
print(numbers)

#4
set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}
intersection = set1.intersection(set2)
result = sorted(intersection)
print(result)

#5
string = 'pythonist'
char_count = {char: string.count(char) for char in set(string)}
print(char_count)


list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
# TODO Оформить решение
list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
max_index=0
max_number=list_numbers[max_index]
for i, value in enumerate(list_numbers):
    max_number=list_numbers[max_index]
    if value>=max_number:
       max_index = i
       max_number=list_numbers[max_index]

last_index=-1
last_number=list_numbers[last_index]

list_numbers[max_index], list_numbers[last_index] = list_numbers[last_index], list_numbers[max_index]

print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]

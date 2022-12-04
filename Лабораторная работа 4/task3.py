def delete(list_, index=None):
    if index == None:
        list_.pop(-1)
    else:
        list_.remove(index)
    return list_

# TODO реализовать функцию удаления элемента из списка по индексу
print(delete([0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
# TODO решение
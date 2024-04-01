def find_insert_position(sorted_array, x):
    low = 0
    high = len(sorted_array) - 1

    while low <= high:
        mid = (low + high) // 2
        if sorted_array[mid] == x:
            return mid
        elif sorted_array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return low


# Пример использования
A = [1, 2, 3, 3, 3, 5]
x = 4
index = find_insert_position(A, x)
print(index)

## worst case: Log 16 base 2 = 14

sorted_items = [1, 2, 4, 5, 7, 10, 32, 400, 504, 1023, 12304, 32401, 324020342, 1203023420420, 1203102310310432, 1023104032402401]

def get_mid_value(low, high):
    return (low + high) // 2

def execute_binary_search(array, search):
    low_index = 0
    high_index = len(array) - 1
    mid_index = get_mid_value(low_index, high_index)

    while low_index <= mid_index:
        if search < array[mid_index]:
            high_index = mid_index - 1
        if search > array[mid_index]:
            low_index = mid_index + 1
        if search == array[mid_index]:
            return search
        mid_index = get_mid_value(low_index, high_index)
    return None

print(execute_binary_search(sorted_items, 1023))

